Name:           python-crc32c
Version:        2.8
Release:        %autorelease
Summary:        A python package implementing the crc32c algorithm in hardware and software

License:        LGPL-2.1-or-later
URL:            https://github.com/ICRAR/crc32c
Source:         %{url}/archive/refs/tags/v%{version}/crc32c-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  help2man

%global _description %{expand:
This package implements the crc32c checksum algorithm. It automatically
chooses between a hardware-based implementation (using theCRC32C SSE
4.2 instruction of Intel CPUs, and the crc32* instructions on ARMv8
CPUs), or a software-based one when no hardware support can be found.}

%description %{_description}


%package -n python3-crc32c
Summary:        %{summary}

%description -n python3-crc32c %{_description}


%prep
%autosetup -n crc32c-%{version}
%generate_buildrequires
%pyproject_buildrequires -g test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l crc32c
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH="%{buildroot}%{python3_sitearch}" help2man \
    --version-string %{version} \
    %{buildroot}%{_bindir}/crc32c | \
    sed 's|\\fI\\,.*\/crc32c\\/\\fP|\\fI\\,crc32c\\/\\fP|g' | \
    gzip > %{buildroot}%{_mandir}/man1/crc32c.1.gz


%check
%pyproject_check_import

%pytest
PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} run-tests.py


%files -n python3-crc32c -f %{pyproject_files}
%doc CHANGELOG.md
%license LICENSE
%license LICENSE.google-crc32c
%license LICENSE.slice-by-8
%doc README.rst
%attr(755,root,root) %{_bindir}/crc32c
%{_mandir}/man1/crc32c.1.gz

%changelog
%autochangelog
