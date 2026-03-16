Name:            aime
Version:         8.20250217
Release:         %autorelease
Summary:         An application embeddable programming language interpreter
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
# workaround for bug 2336032 aime fails to build with GCC 15/C23
%set_build_flags
export CFLAGS="%{optflags} -std=gnu17"
%configure
%make_build

%check
%make_build check

%install
%make_install
# We do not package the static library by default, following Fedora policy
# of not packaging static libraries unless specifically granted an exception.
find %{buildroot} -name '*.a' -delete -print
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING
%doc README TODO
%{_bindir}/aime
%{_bindir}/xe
%{_bindir}/xi
%{_bindir}/xo
%{_infodir}/aime.info*
%{_infodir}/libaime.info*
%{_mandir}/man1/aime.1*
%{_mandir}/man1/xe.1*

%files devel
%doc README TODO
%{_includedir}/%{name}.h

%changelog
%autochangelog
