%global _description\
Lupa integrates the run-times of Lua or LuaJIT2 into CPython. It is a\
partial rewrite of LunaticPython in Cython with some additional features\
such as proper co-routine support.

%ifarch x86_64 aarch64
%bcond_without luajit
%else
%bcond_with luajit
%endif

Name:           python-lupa
Version:        2.6
Release:        %autorelease
Summary:        Python wrapper around Lua and LuaJIT

License:        MIT
URL:            https://pypi.python.org/pypi/lupa
Source:         https://github.com/scoder/lupa/archive/lupa-%{version}/lupa-%{version}.tar.gz
# this could be passed via command line options or envvar if we're invoking setup.py directly
# but we're not
Patch:          lupa-default-to-no-bundle.diff

BuildRequires:  gcc
%if %{with luajit}
BuildRequires:  luajit-devel
%else
BuildRequires:  lua-devel
%endif

%description %_description

%package -n python3-lupa
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-setuptools

%description -n python3-lupa %_description


%prep
%autosetup -n lupa-lupa-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l lupa


%check
# tox tries to do setup.py install and setup.py tes
# running tests directly failed because the local lupa folder
# is not functional prior to the build, which we do elsewhere
mkdir test_dir
cp -pr %{buildroot}%{python3_sitearch}/lupa test_dir
cp -pr lupa/tests test_dir/lupa/
cd test_dir
%{py3_test_envvars} %{python3} -m unittest -v


%files -n python3-lupa -f %{pyproject_files}
%doc README.rst CHANGES.rst INSTALL.rst
#{python3_sitearch}/lupa/
#{python3_sitearch}/lupa-*.egg-info


%changelog
%autochangelog
