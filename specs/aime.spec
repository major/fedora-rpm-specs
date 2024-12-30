%global libname libaime

Name:            aime
Version:         8.20241228
Release:         %autorelease
Summary:         An application embeddable programming language interpreter
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:         GPL-3.0-or-later
URL:             http://aime-embedded.sourceforge.net/
Source0:         http://downloads.sourceforge.net/project/aime-embedded/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:          %{name}-8.20150211-ldflags.patch
BuildRequires:   gcc
BuildRequires:   make

%description
aime is a programming language with a C like syntax, intended for application
extending purposes. The aime collection comprises the language description, an
application embeddable interpreter (libaime), the interpreter C interface
description and a standalone interpreter. Many examples on how the interpreter
can be used (embedded in an application) are also available, together with 
some hopefully useful applications, such as expression evaluators.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description     devel
This package contains header files for developing applications that 
use %{name}.

%prep
%autosetup -p 1

%build
%configure
%make_build

%check
make check

%install
%make_install
find %{buildroot} -name '*.a' -delete -print
rm -frv %{buildroot}%{_infodir}/dir

%files
%doc README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_infodir}/*.info*

%files devel
%{_includedir}/%{name}.h

%changelog
%autochangelog
