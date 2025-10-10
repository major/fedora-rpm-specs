# Currently disabled because the BR isn't available in Fedora
%bcond tests 1

%global forgeurl https://github.com/savoirfairelinux/num2words

%global _description %{expand:
Convert numbers to words in multiple languages, it is a library that converts
numbers like ``42`` to words like ``forty-two``.  It supports multiple
languages (English, French, Spanish, German and Lithuanian) and can even
generate ordinal numbers like ``forty-second``.}

Name:           python-num2words
Version:        0.5.14
Release:        %autorelease
Summary:        Module to convert numbers to words

%forgemeta

# spdx
License:        LGPL-2.0-or-later
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  help2man

%if %{with tests}
# Upstream does not specifically depend on pytest, but it is a convenient test
# runner that allows us to easily skip tests and/or ignore particular files as
# needed.
BuildRequires:  %{py3_dist pytest}
%endif

%description %_description

%package -n python3-num2words
Summary:        %{summary}

%description -n python3-num2words %_description

%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l num2words

# generate man pages
install -d '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man --no-info num2words |
  tee '%{buildroot}%{_mandir}/man1/num2words.1'

%check
%pyproject_check_import
%if %{with tests}
# tests/test_cli.py: requires unpackaged test dependency delegator.py
%pytest --ignore=tests/test_cli.py -v
%endif

%files -n python3-num2words -f %{pyproject_files}
%doc README.rst
%{_bindir}/num2words
%{_mandir}/man1/num2words.1*

%changelog
%autochangelog
