Name:           getmail6
Version:        6.19.9
Release:        %autorelease
Summary:        A mail retrieval, sorting, and delivering system
License:        GPL-2.0-only and Apache-2.0
URL:            https://www.getmail6.org/
Source:         %{pypi_source getmail6}
Patch:          0001-use-multiprocessing-start-method-for-for-tests.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# check
BuildRequires: python3-pytest

%description
A mail retriever with support for POP3, POP3-over-SSL, IMAP4,
IMAP4-over-SSL, and SDPS mail accounts. It supports normal single-user
mail accounts and multidrop (domain) mailboxes.

%prep
%autosetup -p1 -n getmail6-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'getmailcore' +auto

%check
%pyproject_check_import
%pytest

%files -f %{pyproject_files}
%license docs/COPYING
%dir /usr/share/doc/getmail

%changelog
%autochangelog
