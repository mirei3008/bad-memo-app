from django.test import TestCase
from django.urls import reverse
from memos.models import Memo

class MemoViewTests(TestCase):
    def test_list_page_ok(self):
        res = self.client.get(reverse("memo_list"))
        self.assertEqual(res.status_code, 200)

    def test_create_requires_title(self):
        res = self.client.post(reverse("create_memo"), data={"title": "", "body": "x", "tags": ""})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "タイトルは必須")

    def test_memo_detail_nonexistent_returns_404(self):
        """Non-existent memo ID should return 404 instead of 500"""
        res = self.client.get(reverse("memo_detail", args=[99999]))
        self.assertEqual(res.status_code, 404)

    def test_edit_memo_nonexistent_returns_404(self):
        """Non-existent memo ID should return 404 instead of 500"""
        res = self.client.get(reverse("edit_memo", args=[99999]))
        self.assertEqual(res.status_code, 404)

    # TODO: detail/edit/delete / legacy検索 / pagination のテストを追加
