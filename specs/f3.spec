Name:		f3
Version:	10.0
Release:	%autorelease
Summary:	Utility to test for fake flash drives and cards
License:	GPL-3.0-only
URL:		https://oss.digirati.com.br/f3/
Source:		https://github.com/AltraMayor/%{name}/archive/v%{version}/%{name}-%{version}.zip

ExcludeArch:	%{ix86}

BuildRequires: gcc
BuildRequires: make
BuildRequires: parted-devel
BuildRequires: systemd-devel


%description
F3 is a utility to test for fake flash drives and cards. It is a Free
Software alternative to h2testw.  f3write will fill the unused part of
a filesystem with files NNNN.fff with known content, and f3read will
analyze the files to determine whether the contents are corrupted, as
happens with fake flash.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build all extra

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 build/f3read build/f3write build/f3probe build/f3brew build/f3fix %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 man/f3read.1 %{buildroot}%{_mandir}/man1
ln -s f3read.1 %{buildroot}%{_mandir}/man1/f3write.1

%files
%license LICENSE
%doc changelog README.rst
%{_bindir}/f3read
%{_bindir}/f3write
%{_bindir}/f3brew
%{_bindir}/f3fix
%{_bindir}/f3probe
%{_mandir}/man1/f3read.1*
%{_mandir}/man1/f3write.1*

%changelog
%autochangelog
