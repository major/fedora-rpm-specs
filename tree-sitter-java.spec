Name:            tree-sitter-java
Version:         0.20.2

%global forgeurl https://github.com/tree-sitter/%{name}
%forgemeta
%global libname  lib%{name}
%global summary  Java grammar for Tree-sitter
%global desc     Add support for Java to Tree-sitter, an incremental parsing system for \
programming tools.


Release:        %autorelease
Summary:        %{summary}
License:        MIT
URL:            %{forgeurl}

Source:         %{forgesource}

BuildRequires:  gcc
BuildRequires:  libtree-sitter-devel
BuildRequires:  make

%description
%{desc}


%package -n %{libname}
Summary:        %{summary}
Recommends:     libtree-sitter
Enhances:       libtree-sitter

%description -n %{libname}
%{desc}


%package -n %{libname}-devel
Summary:        Development files for %{libname}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname}-devel
Libraries and header files for developing applications that use
%{name}.


%prep
%forgeautosetup


%build
%make_build all


%install
%make_install PARSER_REPO_URL=%{forgeurl} \
              PREFIX=%{_prefix} INCLUDEDIR=%{_includedir} LIBDIR=%{_libdir}
find $RPM_BUILD_ROOT -name '*.a' -delete


%{?ldconfig_scriptlets}


%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/%{libname}.so.*

%files -n %{libname}-devel
%{_includedir}/*
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/*.pc


%changelog
%autochangelog
