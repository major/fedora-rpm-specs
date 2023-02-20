# XXX: note for maintainers
# Do NOT update HDMF without checking if packages that depend on it, for example python-pynwb can be installed with the new version

%bcond_without tests

%global desc %{expand: \
The Hierarchical Data Modeling Framework The Hierarchical Data Modeling
Framework, or *HDMF* is a Python package for working with hierarchical data. It
provides APIs for specifying data models, reading and writing data to different
storage backends, and representing data with Python object.Documentation of
HDMF can be found at Release. Documentation of HDMF can be found at 
https://hdmf.readthedocs.io}

%global pypi_name hdmf

Name:           python-hdmf
Version:        3.5.1
Release:        %autorelease
Summary:        A package for standardizing hierarchical object data

License:        BSD-3-Clause-LBNL
URL:            https://github.com/hdmf-dev/hdmf
Source0:        %{url}/releases/download/%{version}/hdmf-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on help output
Source1:        validate_hdmf_spec.1

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description
%{desc}

%package -n python3-hdmf
Summary:        %{summary}

%description -n python3-hdmf
%{desc}

%prep
%autosetup -n hdmf-%{version} -S patch -p1

# Remove all upper bounds on dependency versions. These are added upstream as a
# matter of course rather than due to known incompatibility, and it is more
# likely that this package will be broken by the upper bounds than by changes
# in new dependency versions.
sed -r -i "s/,<[^']+'/'/" setup.py

find * -type f -name "*.py" -exec sed -i '/^#![ ]*\/usr\/bin\/.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hdmf
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'

%check
%if %{with tests}
%pytest
%endif

%files -n python3-hdmf -f %{pyproject_files}
%license license.txt
%doc README.rst Legal.txt
%{_bindir}/validate_hdmf_spec
%{_mandir}/man1/validate_hdmf_spec.1*

%changelog
%autochangelog
