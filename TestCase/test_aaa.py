#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class Test_11():
    @pytest.mark.aaa
    def test_xue222(self,test_function,test_class,test_module,test_session):
        print("test_xue222")

    @pytest.mark.bbb
    def test_xue111(self,test_function,test_class,test_module,test_session):
        print("test_xue111")

class Test_222():
    def test_xue333(self,test_function,test_class,test_module,test_session):
        print("test_xue333")
    def test_xue444(self,test_function,test_class,test_module,test_session):
        print("test_xue444")