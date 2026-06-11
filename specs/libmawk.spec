Name:           libmawk
Version:        1.0.5
Release:        %autorelease
Summary:        Embed awk scripting language in any application written in C

License:        GPL-2.0-only
URL:            http://repo.hu/projects/libmawk
Source:         http://repo.hu/projects/libmawk/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Libmawk is a fork of mawk 1.3.3 restructured for embedding.
This means the user gets libmawk.h and libmawk.so and can embed
awk scripting language in any application written in C.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
HTML documentation for %{name}.


%prep
%autosetup


%build
# This ./configure command refers to scconfig. See http://repo.hu/projects/scconfig/
./"configure" --prefix=%{_prefix} --libarchdir=%{_lib} --symbols \
  --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}"
%make_build


%install
%make_install LIBARCHDIR=%{buildroot}/%{_libdir} LIBPATH=%{buildroot}/%{_libdir}/%{name}


%check
%make_build test


%files
%license src/libmawk/COPYING
%doc AUTHORS README Release_notes
%{_libdir}/*.so.1
%{_libdir}/*.so.1.0*
%{_bindir}/lmawk
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.awk
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/*.so

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*.html


%changelog
%autochangelog
