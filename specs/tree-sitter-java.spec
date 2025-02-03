Name:            tree-sitter-java
Version:         0.23.5

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

BuildRequires:  (tree-sitter >= 0.24.0 or /usr/bin/g++)
BuildRequires:  /usr/bin/tree-sitter
BuildRequires:  gcc
BuildRequires:  libtree-sitter-devel
BuildRequires:  make
BuildRequires:  tree-sitter-cli >= 0.24.3

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
%make_build all PARSER_URL=%{url}


%install
%make_install PREFIX=%{_prefix} INCLUDEDIR=%{_includedir} LIBDIR=%{_libdir}
find $RPM_BUILD_ROOT -name '*.a' -delete


%check
%{__make} test


%{?ldconfig_scriptlets}


%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/%{libname}.so.*

%files -n %{libname}-devel
%{_includedir}/tree_sitter/%{name}.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
