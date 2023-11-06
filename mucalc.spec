Name:           mucalc
Version:        2.1
Release:        %autorelease
Summary:        Convenient command line calculator

License:        GPL-3.0-or-later
URL:            https://marlam.de/mucalc
Source0:        %{url}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnupg2

BuildRequires:  muParser-devel
BuildRequires:  readline-devel

%description
mucalc is a convenient calculator for the command line. It evaluates
mathematical expressions that are given as arguments, read from an input
stream, or typed interactively. In interactive mode, it provides line editing
with tab-completion and persistent history using GNU readline. The evaluation
of expressions is handled by the muParser math parser library.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
