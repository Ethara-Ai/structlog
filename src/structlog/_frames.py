# SPDX-License-Identifier: MIT OR Apache-2.0
# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the MIT License.  See the LICENSE file in the root of this
# repository for complete details.

from __future__ import annotations

import sys
import traceback

from collections.abc import Callable
from io import StringIO
from types import FrameType

from .contextvars import _ASYNC_CALLING_STACK
from .typing import ExcInfo


def _format_exception(exc_info: ExcInfo) -> str:
    """
    Prettyprint an `exc_info` tuple.

    Shamelessly stolen from stdlib's logging module.
    """
    pass


def _find_first_app_frame_and_name(
    additional_ignores: list[str] | None = None,
    *,
    stacklevel: int | None = None,
    _getframe: Callable[[], FrameType] = sys._getframe,
) -> tuple[FrameType, str]:
    """
    Remove all intra-structlog calls and return the relevant app frame.

    Args:
        additional_ignores:
            Additional names with which the first frame must not start.

        stacklevel:
            After getting out of structlog, skip this many frames.

        _getframe:
            Callable to find current frame. Only for testing to avoid
            monkeypatching of sys._getframe.

    Returns:
        tuple of (frame, name)
    """
    pass


def _format_stack(frame: FrameType) -> str:
    """
    Pretty-print the stack of *frame* like logging would.
    """
    pass
