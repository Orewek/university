# -*- coding: utf-8 -*-
# pylint: disable='wrong-import-order'
# type: ignore
"""Computer vision code."""
from heapq import heappop, heappush

from manim import DOWN, Write, GREEN, Text, Flash, WHITE, RED, YELLOW, Transform, Create, BLACK, UR, LEFT, Graph, BLUE, DL, Scene, UP, DashedLine, GRAY, VGroup, UL, normalize

import numpy as np


class PrimAlgorithm(Scene):
    """Whole algo."""

    def construct(self):
        """."""
        # Настройки сцены
        self.camera.background_color = '#1e1e1e'
        title = Text('Алгоритм Прима', font_size=40).to_edge(UP)
        self.add(title)

        # Разделительная линия
        divider = DashedLine(UP * 3, DOWN * 3, color=GRAY)
        self.add(divider)

        # Легенда цветов
        legend_title = Text('Обозначения цветов:', font_size=24, color=WHITE)
        legend_items = VGroup(
            Text('- Синий: непосещённые вершины', font_size=20, color=BLUE),
            Text('- Жёлтый: рассматриваемые рёбра/вершины', font_size=20, color=YELLOW),
            Text('- Красный: выбранное минимальное ребро', font_size=20, color=RED),
            # Text('- Зелёный: рёбра MST', font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        legend = VGroup(legend_title, legend_items).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        legend.to_corner(UL, buff=0.75)
        self.add(legend)

        # Данные графа
        vertices = ['A', 'B', 'C', 'D', 'E']
        edges = [
            ('A', 'B', 3),
            ('A', 'D', 15),
            ('A', 'E', 20),
            ('B', 'C', 5),
            ('B', 'D', 1),
            ('C', 'D', 18),
            ('D', 'E', 6),
            # ('D', 'F', 1),
            # ('G', 'A', 1),
        ]

        # Создаем граф
        graph = Graph(
            vertices,
            [e[:2] for e in edges],
            layout='circular',
            labels=True,
            label_fill_color=BLACK,
            vertex_config={
                'radius': 0.3,
                'color': BLUE,
                'fill_opacity': 0.7,
                'stroke_width': 2,
            },
            edge_config={
                'stroke_width': 3,
                'stroke_opacity': 0.8,
            },
        ).scale(0.9).to_corner(DL, buff=1)

        # Подписи весов рёбер
        weight_labels = {}
        for u, v, w in edges:
            line = graph.edges[(u, v)]
            direction = normalize(line.get_end() - line.get_start())
            perp = np.array([-direction[1], direction[0], 0])

            weight = Text(str(w), font_size=24, color=WHITE).move_to(line.get_center() + perp * 0.25)
            weight.add_background_rectangle(color=BLACK, opacity=0.7, buff=0.1)
            weight_labels[(u, v)] = weight

        # Правая панель информации
        panel_title = Text('Процесс выбора рёбер', font_size=28, color=YELLOW)
        panel_title.to_corner(UR).shift(LEFT * 1.5 + DOWN * 0.5)

        # Позиции элементов UI
        step_pos = panel_title.get_center() + DOWN * 1.5
        min_pos = step_pos + DOWN * 1.5
        edges_pos = min_pos + DOWN * 1.5

        # Функции для обновления UI
        def update_step_info(step):
            """."""
            return Text(f'Шаг {step}:', font_size=26, color=WHITE).move_to(step_pos)

        def update_min_edge_text(edge):
            """."""
            return Text(
                f'Минимальное: {edge[0]}-{edge[1]} ({edge[2]})',
                font_size=26,
                color=GREEN,
            ).move_to(min_pos)

        def update_edges_list(edge_list):
            """."""
            new_list = VGroup()
            for w, u, v in edge_list:
                edge_text = Text(f'{u}-{v}: {w}', font_size=24)
                new_list.add(edge_text)

            if new_list:
                new_list.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
                new_list.move_to(edges_pos)

            return new_list

        # Инициализация UI
        step_info = update_step_info(1)
        min_edge_text = Text('Минимальное: -', font_size=26, color=GREEN).move_to(min_pos)
        edges_list = VGroup().move_to(edges_pos)

        self.add(panel_title, step_info, min_edge_text, edges_list)

        # Анимация создания графа
        self.play(
            Create(graph),
            *[Create(label) for label in weight_labels.values()],
            run_time=2,
        )
        self.wait(1)

        # Алгоритм Прима
        visited = {'A'}
        mst_edges = []
        step_counter = 1

        while len(visited) < len(vertices):
            # 1. Поиск рёбер с использованием кучи
            heap = []
            [heappush(heap, (w, u, v)) for u, v, w in edges if (u in visited) ^ (v in visited)]
            # 2. Проверка связности
            if not heap:
                warning = Text('Граф несвязный!', color=RED).next_to(panel_title, DOWN)
                self.play(Write(warning))
                self.wait(2)
                break

            # 3. Получение минимального ребра
            w, u, v = heappop(heap)
            min_edge = (u, v, w)

            # 4. Подсветка рассматриваемых рёбер
            self.play(
                Transform(step_info, update_step_info(step_counter)),
                *[weight_labels[(u, v)].animate.set_color(YELLOW) for u, v, _ in edges if (u in visited) ^ (v in visited)],
                run_time=1,
            )
            self.wait(0.5)

            # 5. Подсветка выбранного ребра
            self.play(
                Transform(min_edge_text, update_min_edge_text(min_edge)),
                Transform(edges_list, update_edges_list(heap)),
                graph.edges[min_edge[:2]].animate.set_stroke(color=RED, width=6),
                graph.vertices[u].animate.set_fill(color=YELLOW, opacity=0.5),
                graph.vertices[v].animate.set_fill(color=YELLOW, opacity=0.5),
                weight_labels[min_edge[:2]].animate.set_color(RED),
                run_time=1.5,
            )
            self.wait(1)

            # 6. Добавление в MST
            mst_edges.append(min_edge[:2])
            visited.update(min_edge[:2])

            # 7. Фиксация результата
            self.play(
                graph.edges[min_edge[:2]].animate.set_stroke(color=RED, width=4),
                *[weight_labels[(u, v)].animate.set_color(WHITE) for u, v, _ in edges if (u, v) not in mst_edges],
                run_time=1,
            )

            step_counter += 1

        # Финальная анимация
        self.play(
            *[Flash(vertex, color=GREEN, flash_radius=0.5) for vertex in graph.vertices.values()],
            run_time=2,
        )

        result_text = Text(
            'Минимальное основное дерево построено!',
            font_size=18,
            color=GREEN,
        ).next_to(DOWN, buff=1)

        self.play(Write(result_text))
        self.wait(3)


if __name__ == '__main__':
    scene = PrimAlgorithm()
    scene.render()
