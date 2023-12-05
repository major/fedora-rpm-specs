Name:		asciinema
Version:	2.4.0
Release:	%autorelease
Summary:	Terminal session recorder

License:	GPL-3.0-or-later
URL:		https://asciinema.org
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description
Asciinema is a free and open source solution for recording the terminal sessions
and sharing them on the web.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
# man page
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/asciinema.1 %{buildroot}%{_mandir}/man1/

%check
%pytest -v

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%doc %{_docdir}/%{name}/asciicast-v1.md
%doc %{_docdir}/%{name}/asciicast-v2.md
%{_bindir}/asciinema
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
