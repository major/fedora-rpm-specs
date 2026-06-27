Summary: Python serial port access library
Name: pyserial
Version: 3.5
Release: %autorelease
Source0: %pypi_source
Patch0: 0001-cherry-picked-fixes-from-upstream.patch
License: BSD-3-Clause
URL: https://pypi.org/project/pyserial/
BuildRequires: python3-devel
BuildArch: noarch

%global _description\
This module encapsulates the access for the serial port. It provides backends\
for standard Python running on Windows, Linux, BSD (possibly any POSIX\
compliant system) and Jython. The module named "serial" automatically selects\
the appropriate backend.

%description %_description


%package -n python3-pyserial
Summary: %{summary}
Conflicts: python2-pyserial < 3.4-6

%description -n python3-pyserial %_description


%prep
export UNZIP="-aa"
%autosetup -p1

# Python 3.13+ has removed unittest.findTestCases()
# Reported upstream: https://github.com/pyserial/pyserial/issues/754
sed -i 's/unittest.findTestCases(module)/unittest.TestLoader().loadTestsFromModule(module)/' test/run_all_tests.py

# Remove shebangs from library modules
find serial -name '*.py' -exec sed -i '1{\@^#!/@d}' {} +

# Fix shebangs in example scripts
%py3_shebang_fix examples/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files serial


%check
%pyproject_check_import -e 'serial.serialcli' -e 'serial.serialjava' -e 'serial.serialwin32' -e 'serial.win32' -e 'serial.tools.list_ports_osx' -e 'serial.tools.list_ports_windows' -e 'serial.urlhandler.protocol_cp2110'
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{python3} test/run_all_tests.py


%files -n python3-pyserial -f %{pyproject_files}
%doc LICENSE.txt CHANGES.rst README.rst examples
%{_bindir}/pyserial-miniterm
%{_bindir}/pyserial-ports

%changelog
%autochangelog
