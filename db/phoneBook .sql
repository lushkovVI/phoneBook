-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Фев 25 2020 г., 07:07
-- Версия сервера: 5.7.29-0ubuntu0.18.04.1
-- Версия PHP: 7.2.24-0ubuntu0.18.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `phoneBook`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Contact`
--

CREATE TABLE `Contact` (
  `id` int(11) NOT NULL,
  `idwork` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `blacklist` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Contact`
--

INSERT INTO `Contact` (`id`, `idwork`, `name`, `mail`, `blacklist`) VALUES
(1, 1, 'Vlad', 'vlad@qwe.com', 0),
(12, 6, 'Andrew', 'andrew@bfd.com', 0),
(18, 13, 'dennis', 'dennis@id.com', 1),
(20, 1, 'ivan', 'ivan@we.com', 1),
(21, 1, 'ivane', 'ivan@we.com', 1),
(22, 4, 'Kolya', 'Kolya@23.com', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `Groups`
--

CREATE TABLE `Groups` (
  `id` int(11) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Groups`
--

INSERT INTO `Groups` (`id`, `type`, `note`) VALUES
(1, 'family1', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'),
(2, 'Work1', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'),
(4, 'Work2', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'),
(5, 'Friend3', 'Aenean commodo ligula eget dolor. '),
(6, 'emergency contacts3', 'Aenean commodo ligula eget dolor. '),
(11, 'Educational', 'Sed consequat, leo eget bibendum sodales, augue velit cursus nun'),
(15, 'holydays', ' enc'),
(17, 'holyda23	', ' enco322');

-- --------------------------------------------------------

--
-- Структура таблицы `GroupsContacts`
--

CREATE TABLE `GroupsContacts` (
  `id` int(11) NOT NULL,
  `idcontact` int(11) NOT NULL,
  `idgroup` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `GroupsContacts`
--

INSERT INTO `GroupsContacts` (`id`, `idcontact`, `idgroup`) VALUES
(3, 12, 5),
(4, 18, 6),
(5, 1, 5),
(6, 1, 11),
(7, 20, 15),
(8, 20, 6);

-- --------------------------------------------------------

--
-- Структура таблицы `Phone`
--

CREATE TABLE `Phone` (
  `id` int(11) NOT NULL,
  `number` varchar(20) DEFAULT NULL,
  `idcontact` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Phone`
--

INSERT INTO `Phone` (`id`, `number`, `idcontact`) VALUES
(1, '8-111-111-11-11', 1),
(3, '8 888 88 88', 1),
(4, '8-555-666-22-33', 12),
(5, '8-999-999-99-91', 18),
(6, '456565', 18),
(7, '223344', 20),
(8, '556677', 21),
(9, '889900', 20),
(14, '824646', 22);

-- --------------------------------------------------------

--
-- Структура таблицы `Work`
--

CREATE TABLE `Work` (
  `id` int(11) NOT NULL,
  `post` varchar(100) DEFAULT NULL,
  `companyName` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Work`
--

INSERT INTO `Work` (`id`, `post`, `companyName`) VALUES
(1, 'builder', 'factory'),
(4, 'lawyer', 'LawAndOrder'),
(6, 'Taxi', '555 35 35'),
(12, 'fireman', 'fire station'),
(13, 'professro3232323', 'university'),
(22, 'professro6', '2universi'),
(23, 'policman', 'policistation');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Contact`
--
ALTER TABLE `Contact`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `Contact_ibfk_1` (`idwork`);

--
-- Индексы таблицы `Groups`
--
ALTER TABLE `Groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `type` (`type`);

--
-- Индексы таблицы `GroupsContacts`
--
ALTER TABLE `GroupsContacts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `GroupsContacts_ibfk_1` (`idcontact`),
  ADD KEY `GroupsContacts_ibfk_2` (`idgroup`);

--
-- Индексы таблицы `Phone`
--
ALTER TABLE `Phone`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `number` (`number`),
  ADD KEY `Phone_ibfk_1` (`idcontact`);

--
-- Индексы таблицы `Work`
--
ALTER TABLE `Work`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `post` (`post`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Contact`
--
ALTER TABLE `Contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- AUTO_INCREMENT для таблицы `Groups`
--
ALTER TABLE `Groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT для таблицы `GroupsContacts`
--
ALTER TABLE `GroupsContacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT для таблицы `Phone`
--
ALTER TABLE `Phone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT для таблицы `Work`
--
ALTER TABLE `Work`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `Contact`
--
ALTER TABLE `Contact`
  ADD CONSTRAINT `Contact_ibfk_1` FOREIGN KEY (`idwork`) REFERENCES `Work` (`id`) ON DELETE SET NULL;

--
-- Ограничения внешнего ключа таблицы `GroupsContacts`
--
ALTER TABLE `GroupsContacts`
  ADD CONSTRAINT `GroupsContacts_ibfk_1` FOREIGN KEY (`idcontact`) REFERENCES `Contact` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `GroupsContacts_ibfk_2` FOREIGN KEY (`idgroup`) REFERENCES `Groups` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Phone`
--
ALTER TABLE `Phone`
  ADD CONSTRAINT `Phone_ibfk_1` FOREIGN KEY (`idcontact`) REFERENCES `Contact` (`id`) ON DELETE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
