%global pypi_name cro

%global _description %{expand:
Coral Reefs Optimization (CRO) algorithm artificially simulates a coral reef, 
where different corals (which are the solutions for the considered 
optimization problem) grow and reproduce in a coral-reef, fighting with 
other corals for space and find depredation.}

Name:           python-%{pypi_name}
Version:        0.0.5.0
Release:        5%{?dist}
Summary:        An implementation of CRO metaheuristic algorithm
License:        MIT
URL:            https://github.com/VictorPelaez/coral-reef-optimization-algorithm
Source0:        %{pypi_source %{pypi_name}}

# add LICENSE from upstream -- pypi version does not contain license text
Source1:        %{url}/raw/cb11d529acd929c488bb433f8bb87f5d1988d923/LICENSE.txt

# Encode dependencies in setup.py, and add matplotlib
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/58
#
# This patch file touches requirements.txt, which is not included in the
# PyPI source archive, so we use a modified version that omits the changes
# to requirements.txt.
Patch0:         58-pypi.patch
Patch1:         %{url}/pull/59.patch

# Import Bunch from sklearn.utils
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/63
#
# Fixes:
# Import of Bunch needs to be fixed for recent scikit-learn versions
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/issues/62
Patch2:         %{url}/pull/63.patch
     
BuildArch:      noarch

BuildRequires:  python3-devel

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

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
%pyproject_buildrequires -r

# Add LICENSE.txt to metadata
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/60
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

# Do not install “examples” as a top-level package
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/59
# Patch1:         %{url}/pull/59.patch

%check
# Upstream provides no tests
%pyproject_check_import
# Also use the examples as “smoke tests”
pushd examples
for example in example_*.py
do
  PYTHONPATH='%{buildroot}%{python3_sitelib}' %{python3} "${example}"
done
popd
    
%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.txt examples

%changelog
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
