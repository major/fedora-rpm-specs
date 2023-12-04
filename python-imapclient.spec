%global pypi_name imapclient
%global forgeurl https://github.com/mjs/imapclient/

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        %{autorelease}
Summary:        Easy-to-use, Pythonic and complete IMAP client library
%global tag %{version}
%forgemeta
License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource


BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
IMAPClient is an easy-to-use, Pythonic and complete IMAP client library.

Features:
 - Arguments and return values are natural Python types
 - IMAP server responses are fully parsed and readily usable
 - IMAP unique message IDs (UIDs) are handled transparently
 - Internationalised mailbox names are transparently handled
 - Time zones are correctly handled
 - Convenience methods are provided for commonly used functionality
 - Exceptions are raised when errors occur

Python versions 3.7 through 3.11 are officially supported.

IMAPClient includes comprehensive units tests and automated functional
tests that can be run against a live IMAP server.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Remove shebang (no entry point)
sed -i '/^#!.*python/d' imapclient/interact.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc NEWS.rst README.rst examples


%changelog
%autochangelog
