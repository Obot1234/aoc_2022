import numpy as np

from day import Day
from inputs.converter import NumpyConverter


class Today(Day[int]):
    def __init__(self) -> None:
        super().__init__(8)
        self.forest = NumpyConverter().convert(self.input)

    def part1(self) -> int:
        top = self.get_visible(self.forest)
        left = self.get_visible(self.forest.T).T
        bottom = self.get_visible(self.forest[::-1, ::-1])[::-1, ::-1]
        right = self.get_visible(self.forest[::-1, ::-1].T)[::-1, ::-1].T
        total = top + left + bottom + right
        # self.do_draw(top, left, bottom, right, total, "../artifacts/day8_visible_trees.png")
        return np.sum(total).item()

    def part2(self) -> int:
        top = self.get_viewing_distance(self.forest)
        left = self.get_viewing_distance(self.forest.T).T
        bottom = self.get_viewing_distance(self.forest[::-1, ::-1])[::-1, ::-1]
        right = self.get_viewing_distance(self.forest[::-1, ::-1].T)[::-1, ::-1].T
        total = top * left * bottom * right
        # self.do_draw(np.log(top), np.log(left), np.log(bottom), np.log(right), np.log(total),
        #             "../artifacts/day8_scenic_score.png")
        return np.max(total)

    @staticmethod
    def do_draw(top: np.ndarray, left: np.ndarray, bottom: np.ndarray, right: np.ndarray, total: np.ndarray,
                name: str):
        import matplotlib.pyplot as plt
        from matplotlib import gridspec
        nrow = 3
        ncol = 3
        fig = plt.figure(figsize=(ncol + 1, nrow + 1))

        gs = gridspec.GridSpec(nrow, ncol,
                               wspace=0.0, hspace=0.0,
                               top=1. - 0.5 / (nrow + 1), bottom=0.5 / (nrow + 1),
                               left=0.5 / (ncol + 1), right=1 - 0.5 / (ncol + 1))
        axes = {}
        for x in range(3):
            for y in range(3):
                axes[(x, y)] = plt.subplot(gs[x, y])
                axes[(x, y)].set_axis_off()
        axes[(1, 0)].imshow(left)
        axes[(0, 1)].imshow(top)
        axes[(1, 2)].imshow(right)
        axes[(2, 1)].imshow(bottom)
        axes[(1, 1)].imshow(total)
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.savefig(name, dpi=1000, bbox_inches="tight", transparent=True)

    @staticmethod
    def get_visible(array: np.ndarray) -> np.ndarray:
        ans = np.zeros_like(array).astype(bool)
        ans[0, :] = True
        tallest_tree = array[0, :].copy()
        for k in range(1, array.shape[0]):
            ans[k, :] = array[k, :] > tallest_tree
            tallest_tree[ans[k, :]] = array[k, ans[k, :]].copy()
        return ans

    @staticmethod
    def get_viewing_distance(array: np.ndarray):
        ans = array.copy()
        ans[-1, :] = 100  # make the argmax below always stop at the end row
        for k in range(0, ans.shape[0] - 1):
            ans[k, :] = np.argmax(ans[k, :] <= ans[k + 1:, :], axis=0) + 1
        ans[-1, :] = 0  # and the end row is 0 by definition
        return ans


if __name__ == '__main__':
    Today().lets_go()
