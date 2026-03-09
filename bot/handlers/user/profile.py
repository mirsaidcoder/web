from aiogram import Router
router = Router()

def register(dp):
    dp.include_router(router)