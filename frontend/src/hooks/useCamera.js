import { useState, useRef } from 'react';

export const useCamera = () => {
  const [image, setImage] = useState(null);
  const [showCamera, setShowCamera] = useState(false);
  const webcamRef = useRef(null);

  const captureImage = () => {
    if (webcamRef.current) {
      const imageSrc = webcamRef.current.getScreenshot();
      setImage(imageSrc);
      setShowCamera(false);
      return imageSrc;
    }
    return null;
  };

  const resetCamera = () => {
    setImage(null);
    setShowCamera(false);
  };

  const openCamera = () => {
    setShowCamera(true);
  };

  return {
    image,
    showCamera,
    webcamRef,
    captureImage,
    resetCamera,
    openCamera,
    setImage
  };
};
