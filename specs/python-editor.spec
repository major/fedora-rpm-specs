%global pypi_name python-editor

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-editor
Version:        1.0.4
Release:        %autorelease
Summary:        Programmatically open an editor, capture the result

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/fmoo/python-editor
Source:         https://github.com/fmoo/python-editor/archive/%{version}.tar.gz
BuildArch:      noarch

%description
Programmatically open an editor, capture the result.

%package -n python3-editor
Summary:        Programmatically open an editor, capture the result.

BuildRequires:  python3-devel

%description -n python3-editor
Programmatically open an editor, capture the result.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Change shebang according to Python version
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' editor.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l editor
chmod a+x $RPM_BUILD_ROOT%{python3_sitelib}/editor.py

%check
%pyproject_check_import

%files -n python3-editor -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
