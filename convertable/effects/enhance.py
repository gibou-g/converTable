from skimage.filters import (threshold_mean, threshold_minimum, threshold_otsu,
                             threshold_yen)


class Effects:
    def __init__(self, image):
        self.image = image

    def contrast(self, method):
        pass

    def brightness(self, pct):
        pass

    def sharpen(self):
        pass


class Threshold:
    """implement multiple thresholding methods

        Binarize images using selected thresohlding methods

    Parameters
    -----------
    image: np.ndarray
        input image

    method: {'mean', 'minimum', 'otsu', 'yen'}, default='mean'
        thresholding method to apply to image.

    """

    def __init__(self, image, method):
        self.image = image
        self.method = method

    def apply(self):
        methods = {
            "mean": self._apply_mean(),
            "minimum": self._apply_min(),
            "otsu": self._apply_otsu(),
            "yen": self._apply_yen(),
        }
        return methods[self.method]

    def _apply_mean(self):
        """apply mean thresholding to image

        binarize image using mean threshold value

        Parameters
        ----------
        image: np.array
            input image
        Returns
        -------
        binarized image
        """
        threshold = threshold_mean(self.image)
        return self.image > threshold

    def _apply_min(self):
        """Apply minimum thresholding on image

        Parameters
        -----------
        image: np.ndarray
            input image

        Returns
        --------
        binarized image

        """
        threshold = threshold_minimum
        return self.image > threshold

    def _apply_otsu(self):
        threshold = threshold_otsu(self.image)
        return self.image > threshold

    def _apply_yen(self):
        threshold = threshold_yen(self.image)
        return self.image > threshold
