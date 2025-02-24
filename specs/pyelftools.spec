# main package is archful to run tests everywhere but produces noarch packages
%global         debug_package %{nil}

Summary:        Pure-Python library for parsing and analyzing ELF files
Name:           pyelftools
Version:        0.32
Release:        %autorelease
# elftools/construct is MIT
License:        Unlicense AND MIT
URL:            https://github.com/eliben/pyelftools
Source0:        https://github.com/eliben/pyelftools/archive/v%{version}/%{name}-%{version}.tar.gz
%global _description \
Pure-Python library for parsing and analyzing ELF files\
and DWARF debugging information.
%description   %_description

%package     -n python3-%{name}
Summary:        %{summary}
# https://github.com/eliben/pyelftools/issues/180
Provides:       bundled(python3-construct) = 2.6
BuildRequires:  %{_bindir}/llvm-dwarfdump
BuildRequires:  %{_bindir}/readelf
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name} %_description

%prep
%autosetup
%ifnarch x86_64
rm test/external_tools/llvm-dwarfdump
rm test/external_tools/readelf
%endif

%build
%{py3_build}

%install
%{py3_install}
pushd %{buildroot}%{_bindir}
mv readelf.py pyreadelf-%{python3_version}
ln -s pyreadelf-%{python3_version} pyreadelf-3
ln -s pyreadelf-3 pyreadelf
popd

%check
%{__python3} test/run_all_unittests.py
%{__python3} test/run_examples_test.py
# tests may fail because of differences in output-formatting
# from binutils' readelf.  See:
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#tests
%{__python3} test/run_readelf_tests.py || :

%files -n python3-%{name}
%license LICENSE
%doc CHANGES
%{_bindir}/pyreadelf
%{_bindir}/pyreadelf-%{python3_version}
%{_bindir}/pyreadelf-3
%{python3_sitelib}/elftools
%{python3_sitelib}/pyelftools-*.egg-info

%changelog
%autochangelog
