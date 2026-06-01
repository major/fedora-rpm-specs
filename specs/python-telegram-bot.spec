Name:           python-telegram-bot
Version:        22.7
Release:        %autorelease
Summary:        A pure Python, asynchronous interface for the Telegram Bot API

License:        LGPL-3.0-only
URL:            https://python-telegram-bot.org
Source0:        https://github.com/python-telegram-bot/python-telegram-bot/releases/download/v%{version}/python_telegram_bot-%{version}.tar.gz
Source1:        https://github.com/python-telegram-bot/python-telegram-bot/releases/download/v%{version}/python_telegram_bot-%{version}.tar.gz.sha1
Source2:        https://github.com/python-telegram-bot/python-telegram-bot/releases/download/v%{version}/python_telegram_bot-%{version}.tar.gz.sigstore.json
Patch:          python-telegram-bot-0001-relax-cachetools-version.patch
Patch:          python-telegram-bot-0002-relax-test-dependencies.patch

BuildRequires: python3-beautifulsoup4
BuildRequires: python3-build
BuildRequires: python3-cryptography
BuildRequires: python3-flaky
BuildRequires: python3-pytest
BuildRequires: python3-pytest-asyncio
BuildRequires: python3-pytest-xdist
BuildRequires: python3-pytz
BuildRequires: python3-pytzdata
BuildRequires: python3-tornado
BuildSystem:   pyproject
BuildOption(install): -l telegram
BuildOption(generate_buildrequires): -x callback-data,ext,http2,job-queue,passport,rate-limiter,socks,webhooks

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This library provides a pure Python, asynchronous interface for the Telegram
Bot API. It's compatible with Python versions 3.10+.

In addition to the pure API implementation, this library features several
convenience methods and shortcuts as well as a number of high-level classes to
make the development of bots easy and straightforward. These classes are
contained in the telegram.ext submodule.}

%description %_description

%package -n     python3-telegram-bot
Summary:        %{summary}

%description -n python3-telegram-bot %_description

%pyproject_extras_subpkg -n python3-telegram-bot callback-data,ext,http2,job-queue,passport,rate-limiter,socks,webhooks

%prep -a
find ./src/telegram -name "*.py" -exec sed -i '1{/^#!/d}' {} +
sed -i 1d ./src/telegram/__main__.py ./src/telegram/request/__init__.py

%check -a
# Test main package only, not extras and not tests that need network access
k="${k-}${k+ or} (test_no_passport.py)"
k="${k-}${k+ or} (test_datetime.py)"
k="${k-}${k+ or} (test_defaults.py)"
k="${k-}${k+ or} (test_jobqueue.py)"
k="${k-}${k+ or} (test_applicationbuilder.py)"
k="${k-}${k+ or} (test_ratelimiter.py)"
k="${k-}${k+ or} (test_updater.py)"
k="${k-}${k+ or} (test_callbackdatacache.py)"
%pytest -k "${k-}"

%files -n python3-telegram-bot -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
