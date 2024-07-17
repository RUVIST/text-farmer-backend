from django.test import TestCase

# Create your tests here.
from unittest import TestCase
from unittest.mock import patch, MagicMock

from board.entity.models import Board
from board.service.board_service_impl import BoardServiceImpl


class BoardViewTest(TestCase):
    @patch('board.service.board_service_impl.BoardRepositoryImpl')
    def testList(self, MockBoardRepositoryImpl):
        mockRepository = MockBoardRepositoryImpl.getInstance.return_value
        mockBoardList = [
            Board(boardId=1, title="Test Board 1", content="Content 1"),
            Board(boardId=2, title="Test Board 2", content="Content 2"),
        ]
        mockRepository.list.return_value = mockBoardList

        BoardServiceImpl._BoardServiceImpl__instance = None
        boardService = BoardServiceImpl.getInstance()

        result = boardService.list()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].title, "Test Board 1")
        self.assertEqual(result[1].title, "Test Board 2")

        mockRepository.list.assert_called_once()
