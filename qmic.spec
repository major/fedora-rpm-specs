Name:           qmic
Version:        1.0
Release:        %autorelease
Summary:        QMI IDL compiler

License:        BSD-3-Clause
URL:            https://github.com/andersson/qmic

Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
QMI IDL compiler.

%prep
%autosetup -p1

%build
%make_build prefix="%{_prefix}"

%install
%make_install prefix="%{_prefix}"

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
