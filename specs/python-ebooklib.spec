%global         srcname         ebooklib
%global         forgeurl        https://github.com/aerkalov/ebooklib
Version:        0.18
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Library for handling books in EPUB2/EPUB3 format

License:        AGPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/%{tag}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
# Documentation
BuildRequires:  python3-sphinx

BuildArch: noarch

%global _description %{expand:
EbookLib is a Python library for managing EPUB2/EPUB3 and Kindle files.
It's capable of reading and writing EPUB files programmatically.

The API is designed to be as simple as possible, while at the same time
making complex things possible too. It has support for covers, table of
contents, spine, guide, metadata and etc.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires
# TODO: build documentation

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ebooklib -L

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%doc AUTHORS.txt
%doc CHANGES.txt
%doc samples
%license LICENSE.txt

%changelog
%autochangelog
