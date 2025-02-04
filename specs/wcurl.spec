%bcond tests 0

Name:           wcurl
Version:        2024.12.08
Release:        %autorelease
Summary:        A simple wrapper around curl to easily download files
License:        curl
BuildArch:      noarch
URL:            https://github.com/curl/%{name}
Source:		%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# rhbz#1992804
# Temporarily disable the test until the PR is merged.
# https://src.fedoraproject.org/rpms/shunit2/pull-request/1
%if %{with tests}
BuildRequires:  shunit2
%endif
BuildRequires:  curl
Requires:       curl

%description
%{summary}.

%prep
%autosetup

%build

%install
install -t '%{buildroot}%{_bindir}' -D -p wcurl
install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p wcurl.1

%check
%if %{with tests}
PATH="${PATH}:%{buildroot}%{_bindir}" ./tests/tests.sh
%endif

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%license AUTHORS
%{_bindir}/wcurl
%{_mandir}/man1/wcurl.1*

%changelog
%autochangelog
