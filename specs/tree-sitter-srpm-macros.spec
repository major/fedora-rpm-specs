Name:           tree-sitter-srpm-macros
Version:        0.4.0
Release:        %autorelease
Summary:        RPM macros for Tree-sitter parsers
License:        MIT
Source0:        MIT.txt
Source1:        README.md
Source2:        macros.tree_sitter
Source3:        tree_sitter.attr
BuildArch:      noarch
Requires:       rpm


%description
RPM macros for building packages for Tree-sitter parsers.


%install
install -Dp -m u=rw,go=r \
        %SOURCE0 %{buildroot}%{_defaultlicensedir}/%{name}/%{basename:%SOURCE0}
install -Dp -m u=rw,go=r \
        %SOURCE1 %{buildroot}%{_pkgdocdir}/%{basename:%SOURCE1}
install -Dp -m u=rw,go=r \
        %SOURCE2 %{buildroot}%{_rpmmacrodir}/%{basename:%SOURCE2}
install -Dp -m u=rw,go=r \
        %SOURCE3 %{buildroot}%{_fileattrsdir}/%{basename:%SOURCE3}


%files
%license %{_defaultlicensedir}/%{name}/
%doc %{_pkgdocdir}/
%{_rpmmacrodir}/%{basename:%SOURCE2}
%{_fileattrsdir}/%{basename:%SOURCE3}


%changelog
%autochangelog
