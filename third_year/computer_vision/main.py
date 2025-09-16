# -*- coding: utf-8 -*-
# pylint: disable='wrong-import-order'
# type: ignore
"""Computer vision code."""
from heapq import heappop, heappush

from manim import (
    BLACK,
    BLUE,
    Create,  # Animation for creating objects
    DashedLine,
    DL,
    DOWN,
    Flash,  # Flash animation effect
    GRAY,
    GREEN,
    LEFT,
    RED,
    Scene,  # Base class for animation scenes
    Text,  # Text object for displaying text
    Transform,  # Transformation animation
    UL,
    UP,
    UR,
    WHITE,
    Write,  # Write animation for text
    YELLOW,
    Graph,  # Graph object for graph visualization
    VGroup,  # Group for managing multiple objects together
    normalize,  # Function for vector normalization
)

import numpy as np

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from numpy import ndarray


class PrimAlgorithm(Scene):
    """Whole algo."""

    def construct(self):
        """."""
        # Scene settings
        # Set dark gray background color for the scene
        self.camera.background_color = '#1e1e1e'
        # Add title text at the top of the scene
        self.add(Text('Алгоритм Прима', font_size=40).to_edge(UP))

        # Divider line
        self.add(DashedLine(UP * 3, DOWN * 3, color=GRAY))

        # Color legend
        legend_title = Text('Обозначения цветов:', font_size=24, color=WHITE)
        # Legend title text
        legend_items = VGroup(
            Text(
                'Синий: непосещённые вершины',
                font_size=20,
                color=BLUE,
            ),
            Text(
                'Жёлтый: рассматриваемые рёбра/вершины',
                font_size=20,
                color=YELLOW,
            ),
            Text(
                'Красный: выбранное минимальное ребро',
                font_size=20,
                color=RED,
            ),
            # Text('- Зелёный: рёбра MST', font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        # Arrange items vertically with left alignment

        # Combine title and items into one group
        legend = VGroup(
            legend_title,
            legend_items,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        # Position legend in upper-left corner
        legend.to_corner(UL, buff=0.75)
        # Add legend to the scene
        self.add(legend)

        # List of graph vertices
        vertices: list[str] = ['A', 'B', 'C', 'D', 'E']
        # List of edges with weights
        edges: list[tuple[str]] = [
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

        # Create graph object
        graph = Graph(
            vertices,  # Vertex list
            # Edge list (vertex pairs only, no weights)
            [e[:2] for e in edges],
            layout='circular',  # Circular layout for vertices
            labels=True,  # Show vertex labels
            label_fill_color=BLACK,  # # Label background color
            vertex_config={
                'radius': 0.3,  # Vertex radius
                'color': BLUE,  # Vertex color
                'fill_opacity': 0.7,  # Fill opacity
                'stroke_width': 2,  # Border width
            },
            edge_config={
                'stroke_width': 3,  # Line width
                'stroke_opacity': 0.8,  # Line opacity
            },
        ).scale(0.9).to_corner(DL, buff=1)
        # Dictionary to store weight labels

        # Подписи весов рёбер
        # For each edge:
        weight_labels: dict = {}
        for u, v, w in edges:
            # Get the edge line object
            line = graph.edges[(u, v)]
            # Calculate normalized direction vector of the edge
            direction: 'ndarray' = normalize(line.get_end() - line.get_start())
            # Calculate perpendicular vector for label offset
            perp = np.array([-direction[1], direction[0], 0])
            # Create weight text and position it offset from edge center
            weight = Text(
                str(w),
                font_size=24,
                color=WHITE,
            ).move_to(line.get_center() + perp * 0.25)
            # Add semi-transparent background for better readability
            weight.add_background_rectangle(color=BLACK, opacity=0.7, buff=0.1)
            # Store label in dictionary
            weight_labels[(u, v)] = weight

        # Right panel information
        panel_title = Text('Процесс выбора рёбер', font_size=28, color=YELLOW)
        # Panel title in upper-right corner
        panel_title.to_corner(UR).shift(LEFT * 1.5 + DOWN * 0.5)

        # UI element positions
        step_pos: ndarray = panel_title.get_center() + DOWN * 1.5
        min_pos: ndarray = step_pos + DOWN * 1.5
        # Define positions for different UI elements
        edges_pos: ndarray = min_pos + DOWN * 1.5

        # UI update functions
        def update_step_info(step: int):
            """."""
            # Update step information text
            return Text(f'Шаг {step}:', font_size=26, color=WHITE).move_to(step_pos)

        def update_min_edge_text(edge: tuple):
            """."""
            # Update minimum edge information text
            return Text(
                f'Минимальное: {edge[0]}-{edge[1]} ({edge[2]})',
                font_size=26,
                color=GREEN,
            ).move_to(min_pos)

        def update_edges_list(edge_list: list):
            """."""
            # Create new group for edge list
            new_list = VGroup()
            for w, u, v in edge_list:
                # Add text representation for each edge
                new_list.add(Text(f'{u}-{v}: {w}', font_size=24))

            if new_list:
                new_list.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
                # Arrange and position the list
                new_list.move_to(edges_pos)

            # Update list of candidate edges
            return new_list

        # UI initialization
        # Initial step information
        step_info = update_step_info(1)
        # Initial minimum edge text
        min_edge_text = Text(
            'Минимальное: -',
            font_size=26,
            color=GREEN,
        ).move_to(min_pos)

        # Empty edges list
        edges_list = VGroup().move_to(edges_pos)

        # Add UI elements to scene
        self.add(panel_title, step_info, min_edge_text, edges_list)

        # Graph creation animation
        self.play(
            Create(graph),  # Animate graph creation
            # Animate weight labels creation
            *[Create(lbl) for lbl in weight_labels.values()],
            run_time=2,  # Animation duration: 2 seconds
        )
        self.wait(1)

        # Prim's algorithm implementation
        visited: set = {'A'}
        # List of edges in Minimum Spanning Tree
        mst_edges: list = []
        # Step counter
        step_counter: int = 1

        # While not all vertices are visited:
        while len(visited) < len(vertices):
            # 1. Find edges using min-heap
            # Create min-heap for edges prioritized by weight
            heap = []
            # Add edges connecting visited and unvisited vertices to heap
            [heappush(heap, (w, u, v)) for u, v, w in edges if (u in visited) ^ (v in visited)]
            # 2. Connectivity check
            if not heap:
                # If heap is empty - graph is disconnected
                self.play(
                    Write(
                        Text(
                            'Граф несвязный!',
                            color=RED,
                        ).next_to(panel_title, DOWN),
                    ),
                )
                self.wait(2)
                break

            # 3. Get minimum weight edge
            # Extract edge with minimum weight from heap
            w, u, v = heappop(heap)
            # Store minimum edge information
            min_edge: tuple = (u, v, w)

            # 4. Highlight candidate edges
            self.play(
                # Update step number
                Transform(step_info, update_step_info(step_counter)),
                # Highlight candidate edges in yellow
                *[weight_labels[(u, v)].animate.set_color(YELLOW) for u, v, _ in edges if (u in visited) ^ (v in visited)],
                run_time=1,
            )
            self.wait(0.5)

            # 5. Highlight selected edge
            self.play(
                #  Update min edge info
                Transform(min_edge_text, update_min_edge_text(min_edge)),
                # Update edges list
                Transform(edges_list, update_edges_list(heap)),
                # Highlight selected edge in red
                graph.edges[min_edge[:2]].animate.set_stroke(
                    color=RED,
                    width=6,
                ),
                # Highlight vertices
                graph.vertices[u].animate.set_fill(color=YELLOW, opacity=0.5),
                graph.vertices[v].animate.set_fill(color=YELLOW, opacity=0.5),
                # Highlight edge weight
                weight_labels[min_edge[:2]].animate.set_color(RED),
                run_time=1.5,
            )
            self.wait(1)

            # 6. Add to MST
            # Add edge to MST
            mst_edges.append(min_edge[:2])
            # Add vertices to visited set
            visited.update(min_edge[:2])

            # 7. Finalize result
            self.play(
                # Set final edge color
                graph.edges[min_edge[:2]].animate.set_stroke(
                    color=RED,
                    width=4,
                ),
                # Reset other weights to white
                *[weight_labels[(u, v)].animate.set_color(WHITE) for u, v, _ in edges if (u, v) not in mst_edges],
                run_time=1,
            )
            # Increment step counter
            step_counter += 1

        # Final animation
        self.play(
            # Flash animation for all vertices
            *[Flash(vertex, color=GREEN, flash_radius=0.5) for vertex in graph.vertices.values()],
            run_time=2,
        )

        self.play(
            Write(
                # Success message
                Text(
                    'Минимальное остовное дерево построено!',
                    font_size=18,
                    color=GREEN,
                ).next_to(DOWN, buff=1)
            ),
        )
        self.wait(3)


if __name__ == '__main__':
    # Render the scene when script is executed directly
    PrimAlgorithm().render()
