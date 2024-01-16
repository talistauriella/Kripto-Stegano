-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 05:11 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `steganografi`
--

-- --------------------------------------------------------

--
-- Table structure for table `embedded_files`
--

CREATE TABLE `embedded_files` (
  `id` int(255) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `output_image_name` varchar(100) NOT NULL,
  `output_file_path` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `embedded_files`
--

INSERT INTO `embedded_files` (`id`, `date`, `output_image_name`, `output_file_path`) VALUES
(1, '2024-01-13 18:30:56', 'output_image (12).png', 'If you have a different type of document, you might need to use a different library or approach. Ple'),
(2, '2024-01-13 18:30:56', 'output_image (12).png', '0100100101100110001000000111100101101111011101010010000001101000011000010111011001100101001000000110'),
(3, '2024-01-13 18:30:56', 'output_image (13).png', 'If you have a different type of document, you might need to use a different library or approach. Ple'),
(4, '2024-01-13 18:30:56', 'output_image (14).png', 'Tema : Ibadah Sholat\nJudul : Pentingnya Kesadaran Mahasiswa Terhadap Sholat dan Pengaruhnya bagi Keb'),
(5, '2024-01-13 18:30:56', 'output_image (15).png', ''),
(6, '2024-01-13 18:30:56', 'output_image (10).png', ''),
(7, '2024-01-13 18:30:56', 'output_image (13).png', ''),
(8, '2024-01-13 18:30:56', 'output_image (16).png', ''),
(9, '2024-01-13 18:30:56', 'output_image (13).png', 'If you have a different type of document, you might need to use a different library or approach. Ple'),
(10, '2024-01-13 18:30:56', 'output_image (17).png', 'If you have a different type of document, you might need to use a different library or approach. Ple'),
(11, '2024-01-15 14:46:09', 'output_image (29).png', 'Nama 		: Talista Auriella Haliana\nNim 		: A11.2022.14495\nKelompok 	: A11.43UG1\nUTS Pendidikan Kewarg');

-- --------------------------------------------------------

--
-- Table structure for table `embedded_images`
--

CREATE TABLE `embedded_images` (
  `id` int(255) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `image_name` varchar(100) NOT NULL,
  `text_name` varchar(100) NOT NULL,
  `output_image_path` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `embedded_images`
--

INSERT INTO `embedded_images` (`id`, `date`, `image_name`, `text_name`, `output_image_path`) VALUES
(1, '2024-01-13 18:29:28', 'test.png', 'example.docx', 'output_image.png'),
(2, '2024-01-13 18:29:28', 'test.png', 'example.docx', 'output_image.png'),
(3, '2024-01-13 18:29:28', 'test.png', 'example.docx', 'output_image.png'),
(4, '2024-01-13 18:29:28', 'output_image (11).png', 'output_image (11).png', 'If you have a different type of document, you might need to use a different library or approach. Ple'),
(5, '2024-01-13 18:29:28', 'test.png', 'example.docx', 'output_image.png'),
(6, '2024-01-13 18:29:28', 'test.png', 'example.docx', 'output_image.png'),
(7, '2024-01-13 18:29:28', 'test.png', 'A11.2022.14495_Talista Auriella Haliana_A11.43UG1.docx', 'output_image.png'),
(8, '2024-01-13 18:29:28', 'test.png', 'example.docx', 'output_image.png'),
(9, '2024-01-13 18:29:28', 'test.png', 'example.docx', 'output_image.png'),
(10, '2024-01-13 18:29:28', 'test.png', 'example.docx', 'output_image.png'),
(11, '2024-01-13 18:29:51', 'test.png', 'example.docx', 'output_image.png'),
(12, '2024-01-15 14:43:08', 'WhatsApp Image 2024-01-15 at 21.21.18_e5684525.jpg', 'UTS_Talista.docx', 'output_image.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `embedded_files`
--
ALTER TABLE `embedded_files`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `embedded_images`
--
ALTER TABLE `embedded_images`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `embedded_files`
--
ALTER TABLE `embedded_files`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `embedded_images`
--
ALTER TABLE `embedded_images`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
