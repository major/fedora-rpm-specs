%global pypi_name FVS

Name:           python-fvs
Version:        0.3.4
Release:        %{autorelease}
Summary:        File Versioning System with hash comparison and data storage
BuildArch:      noarch
License:        MIT
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %{pypi_source %{pypi_name}}
BuildRequires:  python3-devel

%global _description %{expand:
File Versioning System with hash comparison and data storage to create
unlinked states that can be deleted.

Why FVS?

The main reason for this project is for the purpose of personal
knowledge and understanding of the versioning system. The second reason
is to make a simple and easy-to-implement versioning system for
Bottles.

There are plenty of other versioning systems out there, but all of
these provide features that I wouldn't need in my projects. The purpose
of FVS is to always remain as clear and simple as possible, providing
only the functionality of organizing file versions into states, ie
recovery points that take advantage of deduplication to minimize space
consumption.}

%description %_description


%package -n python3-fvs
Summary:        %{summary}
Provides:       fvs = %{?epoch:%{epoch}:}%{version}-%{release}


%description -n python3-fvs %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fvs


%check
# Package does not provide any tests
# https://github.com/mirkobrombin/FVS/issues/2
%pyproject_check_import


%files -n python3-fvs -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/fvs


%changelog
%autochangelog
