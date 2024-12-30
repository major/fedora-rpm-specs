%global pypi_name nihtest
%global forgeurl https://github.com/nih-at/nihtest

%bcond_without tests

Name:           python-%{pypi_name}
Version:        1.9.1
Release:        %{autorelease}
Summary:        A testing tool for command line utilities
%forgemeta
License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource
Patch:          run_tests_using_cmake_and_ctest.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  git-core
# For generating manpages
BuildRequires:  make, mandoc
# For running tests using CMake
%if %{with tests}
BuildRequires:  cmake, gcc
%endif

%global _description %{expand:
This is nihtest, a testing tool for command line utilities.

Tests are run in a sandbox directory to guarantee a clean separation of
the test.

It checks that exit code, standard and error outputs are as expected
and compares the files in the sandbox after the run with the expected
results.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}
Provides:       nihtest = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version} -S git

# Work around issue with package discovery due to SPECPARTS dir
# https://github.com/rpm-software-management/rpm/issues/2532
# Another option seems to be to remove that dir
echo -e '\n[tool.setuptools]\npackages = ["nihtest"]\n' >> pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Generate man pages and docs
pushd manpages
make %{?_smp_mflags}
popd


%install
%pyproject_install
%pyproject_save_files %{pypi_name}

mkdir -p %{buildroot}/%{_mandir}/man{1,5}
mv manpages/nihtest.man manpages/nihtest.1
mv manpages/nihtest-case.man manpages/nihtest-case.5
mv manpages/nihtest.conf.man manpages/nihtest.conf.5
cp -a manpages/*.1 %{buildroot}/%{_mandir}/man1
cp -a manpages/*.5 %{buildroot}/%{_mandir}/man5


%check
%pyproject_check_import

# Run tests using CMake
%if %{with tests}
  # Solution for running tests provided by Benson Muite
  touch check.sh
  echo "PATH=%{buildroot}%{_bindir}:${PATH} PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:${PYTHONPATH} %{python3} %{buildroot}%{_bindir}/nihtest -v \$1 " >> check.sh
  sed -i 's|${NIHTEST}|bash %{_builddir}/%{pypi_name}-%{version}/check.sh|g' tests/CMakeLists.txt
  sed -i 's|ENVIRONMENT "PATH=${path}"|ENVIRONMENT "PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$ENV{PYTHONPATH}"|g' tests/CMakeLists.txt
  echo "PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" >> tests/nihtest.conf.in
  %cmake
  %cmake_build
  %ctest
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*
%doc manpages/*.html
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}.1*
%{_mandir}/man5/%{pypi_name}*.5*


%changelog
%autochangelog
