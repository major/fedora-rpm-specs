Name:           python-pytest-subprocess
Version:        1.5.3
Release:        %autorelease
Summary:        A plugin to fake subprocess for pytest

License:        MIT
URL:            https://github.com/aklajnert/pytest-subprocess
Source0:        %{url}/archive/%{version}/pytest-subprocess-%{version}.tar.gz

# Fix compatibilty with Py 3.14
Patch:          https://github.com/aklajnert/pytest-subprocess/commit/be30d9a94ba45afb600717e3fcd95b8b2ff2c60e.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The plugin adds the fake_subprocess fixture. It can be used it to register
subprocess results so you won't need to rely on the real processes.
The plugin hooks on the subprocess.Popen(), which is the base for other
subprocess functions. That makes the subprocess.run(), subprocess.call(),
subprocess.check_call() and subprocess.check_output() methods also functional.}

%description %_description

%package -n python3-pytest-subprocess
Summary:        %{summary}

%description -n python3-pytest-subprocess %_description


%prep
%autosetup -p1 -n pytest-subprocess-%{version}
# avoid unneeded test dependencies
sed -Ei '/\bcoverage\b/d' setup.py

# Don't turn warning into errors when running tests
# https://github.com/aklajnert/pytest-subprocess/issues/146
sed -i '/error/d' pytest.ini


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_subprocess


%check
%pytest


%files -n python3-pytest-subprocess -f %{pyproject_files}
%doc README.rst HISTORY.rst


%changelog
%autochangelog
