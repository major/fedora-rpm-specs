Name:           hexer
Version:        1.0.6
Release:        2%{?dist}
Summary:        Interactive binary editor

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://devel.ringlet.net/editors/hexer/
Source0:        http://devel.ringlet.net/files/editors/hexer/hexer-1.0.6.tar.xz

Patch1: error_msg_fix.patch

BuildRequires:	gcc
BuildRequires:  ncurses-devel
BuildRequires: make

%description
Hexer is an interactive binary editor (also known as a hex-editor)
with a Vi-like interface. Its most important features are multiple buffers,
multiple-level undo, command-line editing with completion, and binary regular
expressions.

%prep
%setup -q

#%%patch -P1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}/
cp -p hexer %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p hexer.1 %{buildroot}%{_mandir}/man1/

%files
%doc README
%license COPYRIGHT
%{_bindir}/hexer
%{_mandir}/man1/hexer.1*

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
