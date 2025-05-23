Name:           getmail
Version:        6.19.7
Release:        %autorelease
Summary:        A mail retrieval, sorting, and delivering system
License:        GPL-2.0-only and Apache-2.0
URL:            https://www.getmail6.org/
Source:         %{pypi_source getmail}
Patch:          https://github.com/getmail6/getmail6/commit/082d72fa2e83f12b9cce1e2f06ffaf379230348c.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A mail retriever with support for POP3, POP3-over-SSL, IMAP4,
IMAP4-over-SSL, and SDPS mail accounts. It supports normal single-user
mail accounts and multidrop (domain) mailboxes.

%prep
%autosetup -p1 -n getmail-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'getmailcore' +auto

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license docs/COPYING

%changelog
%autochangelog
