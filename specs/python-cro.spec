%global pypi_name cro

%global _description %{expand:
Coral Reefs Optimization (CRO) algorithm artificially simulates a coral reef, 
where different corals (which are the solutions for the considered 
optimization problem) grow and reproduce in a coral-reef, fighting with 
other corals for space and find depredation.}

Name:           python-%{pypi_name}
Version:        0.0.5.2
Release:        8%{?dist}
Summary:        An implementation of CRO metaheuristic algorithm
License:        MIT
URL:            https://github.com/VictorPelaez/coral-reef-optimization-algorithm
Source0:        %{pypi_source %{pypi_name}}

# add LICENSE from upstream -- pypi version does not contain license text
#
# License file is not distributed in sdist
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/issues/71
#
# Add the license file to MANIFEST.i
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/72
Source1:        %{url}/raw/cb11d529acd929c488bb433f8bb87f5d1988d923/LICENSE.txt

# Add missing dependency on “multiprocess”
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/74
Patch:          %{url}/pull/74.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  dos2unix

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -N -n %{pypi_name}-%{version}
# Fix CRNL line endings
find . -type f \( -name '*.py' -o -name '*.csv' -o -name '*.txt'  \) -print0 |
  xargs -r -t -0 dos2unix --keepdate
%autopatch -p1

# Remove shebangs from modules in site-packages. These are not executable
# in the source tarball, and lack “script-like” content.  The
# find-then-modify pattern keeps us from discarding mtimes on sources that
# do not need modification.
find cro -type f -exec \
   gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'

chmod -v a+x examples/example_*.py
%py3_shebang_fix examples
          
%generate_buildrequires
%pyproject_buildrequires

# Add LICENSE.txt to metadata
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/60
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%check
# Upstream provides no tests
%pyproject_check_import
# Also use the examples as “smoke tests”
for example in examples/example_*.py
do
  %{py3_test_envvars} %{python3} "${example}"
done
    
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt examples/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.5.2-4
- Assert a license file is automatically handled; don’t package a duplicate

* Wed Oct 18 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.5.2-3
- F38+: Use %%{py3_test_envvars} to run examples
- Preserve timestamps when fixing line endings

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.5.2-1
- Update to 0.0.5.2 (close RHBZ#2220174)

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 0.0.5.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 0.0.5.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 31 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.5.0-1
- Initial package
