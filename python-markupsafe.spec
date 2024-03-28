Name:           python-markupsafe
Version:        2.1.5
Release:        %autorelease
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source:         https://github.com/pallets/markupsafe/archive/%{version}/markupsafe-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.}

%description %_description


%package -n python3-markupsafe
Summary:        %{summary}

%description -n python3-markupsafe %_description


%prep
%autosetup -n markupsafe-%{version}
# Exclude C source from the package:
echo 'global-exclude *.c' >> MANIFEST.in


%generate_buildrequires
%pyproject_buildrequires requirements/tests.in


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files markupsafe


%check
%pytest


%files -n python3-markupsafe -f %{pyproject_files}
%doc CHANGES.rst README.rst


%changelog
%autochangelog
