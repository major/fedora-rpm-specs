Name:           hexer
Version:        1.0.7
Release:        1%{?dist}
Summary:        Interactive binary editor

License:        BSD-2-Clause AND BSD-3-Clause
URL:            http://devel.ringlet.net/editors/hexer/
Source0:        http://devel.ringlet.net/files/editors/hexer/hexer-%{version}.tar.xz

# Fix "passing argument from incompatible pointer type"
Patch0:         0000-sighandler.patch

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:  ncurses-devel

%description
Hexer is an interactive binary editor (also known as a hex-editor)
with a Vi-like interface. Its most important features are multiple buffers,
multiple-level undo, command-line editing with completion, and binary regular
expressions.

%prep
%autosetup -p1

%build
%make_build PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}/
cp -p hexer %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p hexer.1 %{buildroot}%{_mandir}/man1/

%files
%doc README.md
%license LICENSES/*
%{_bindir}/hexer
%{_mandir}/man1/hexer.1*

%changelog
%autochangelog
