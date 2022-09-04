from subprocess import run

run('clear')
print('0) Обновить зеркала')
print('1) Обновить систему')
print('2) Очистить систему')

num = input('==> Введите цифру что нужно сделать: ')

while num not in ['0', '1', '2']:
	print('Некоректный ввод')
	num = input('==> Введите цифру что нужно сделать: ')

if num == '0':
	run('clear')
	print('Обновление зеркал...')
	try:
		run('sudo reflector --verbose -c ua,pl,ro -l 10 -p https -a 24 \
			--download-timeout 2 --sort rate --save /etc/pacman.d/mirrorlist', \
			shell=True, check=True)
		print('\n** Обновление зеркал выполнено успешно **\n')
	except:
		print('\n** Обновление зеркал не удалось **\n')
elif num == '1':
	run('clear')
	print('Обновление системы...')
	try:
		run('sudo pacman -Syyu --noconfirm', shell=True, check=True)
		print('\n** Обновление системы выполнено успешно **\n')
	except:
		print('\n** Обновление системы не удалось **\n')
elif num == '2':
	run('clear')
	print('Очистка системы...')
