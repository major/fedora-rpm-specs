%global glib2_version 2.45.8

Summary:   Library for querying compressed XML metadata
Name:      libxmlb
Version:   0.3.10
Release:   2%{?dist}
License:   LGPLv2+
URL:       https://github.com/hughsie/libxmlb
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk-doc
BuildRequires: libstemmer-devel
BuildRequires: meson
BuildRequires: gobject-introspection-devel
BuildRequires: xz-devel
BuildRequires: python3-setuptools

# needed for the self tests
BuildRequires: shared-mime-info

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: shared-mime-info

%description
XML is slow to parse and strings inside the document cannot be memory mapped as
they do not have a trailing NUL char. The libxmlb library takes XML source, and
converts it to a structured binary representation with a deduplicated string
table -- where the strings have the NULs included.

This allows an application to mmap the binary XML file, do an XPath query and
return some strings without actually parsing the entire document. This is all
done using (almost) zero allocations and no actual copying of the binary data.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package tests
Summary: Files for installed tests

%description tests
Executable and data files for installed tests.

%prep
%setup -q

%build

%meson \
    -Dgtkdoc=true \
    -Dtests=true

%meson_build

%check
%meson_test

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/xb-tool
%{_mandir}/man1/xb-tool.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Xmlb-2.0.typelib
%{_libdir}/libxmlb.so.2*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Xmlb-2.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libxmlb
%{_includedir}/libxmlb-2
%{_libdir}/libxmlb.so
%{_libdir}/pkgconfig/xmlb.pc

%files tests
%dir %{_libexecdir}/installed-tests/libxmlb
%{_libexecdir}/installed-tests/libxmlb/xb-self-test
%{_libexecdir}/installed-tests/libxmlb/test.xml.gz.gz.gz
%dir %{_datadir}/installed-tests/libxmlb
%{_datadir}/installed-tests/libxmlb/libxmlb.test

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 11 2022 Richard Hughes <richard@hughsie.com> 0.3.10-1
- New upstream release
- Fix dumping and exporting multiple files from the CLI
- Watch files before loading them into the builder
- Fix potential double free when filtering by language

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 Richard Hughes <richard@hughsie.com> 0.3.9-1
- New upstream release
- Fix the crash for when the root tree has no children
- Fix the crash when getting the element for the [empty] root
- Install xb-tool into bindir

* Wed Feb 16 2022 Richard Hughes <richard@hughsie.com> 0.3.7-1
- New upstream release
- Ensure reproducible results when importing a node
- Ignore all hidden files when using _WATCH_DIRECTORY
- Show the value bindings when using XB_SILO_PROFILE_FLAG_XPATH

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Richard Hughes <richard@hughsie.com> 0.3.6-1
- New upstream release
- Ensure _IS_TOKENIZED is set if tokens are added manually
- Ensure we never add too many tokens to the silo

* Wed Dec 01 2021 Richard Hughes <richard@hughsie.com> 0.3.5-1
- New upstream release
- Put tail after the node when exporting XbBuilderNode
- Remove the G_ALIGNOF checks to fix compile with old GLib versions

* Mon Nov 29 2021 Richard Hughes <richard@hughsie.com> 0.3.4-1
- New upstream release
- Add a flag to require the XbBuilderSource to have no siblings
- Add iterator for XbNode attributes and children
- Allow removing XbBuilderNode text
- Allow stripping builder node inner text

* Wed Oct 06 2021 Richard Hughes <richard@hughsie.com> 0.3.3-1
- New upstream release
- Add locking for file monitors
- Add support for LZMA decompression
- Clarify GMainContext usage and signal emission

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Richard Hughes <richard@hughsie.com> 0.3.2-1
- New upstream release
- Respect XB_BUILDER_NODE_FLAG_IGNORE when exporting
- Use the chosen chunk size when reading from a stream
- Use the correct pkgconfig export package name in the GIR file

* Thu May 06 2021 Richard Hughes <richard@hughsie.com> 0.3.1-1
- New upstream release
- Always run xb-tool queries with the optimizer
- Ensure tokens handling works when XbOpcode is not zero-inited
- Use stack-allocated XbStack instances for running a machine

* Fri Mar 12 2021 Richard Hughes <richard@hughsie.com> 0.3.0-1
- New upstream release
- Add a new object to contain query context data
- Allow collapsing empty XML tags if no children or text
- Allow marking elements as tokenized from xb-tool
- Allow optimized searching when comparing tokens
- Cancel the GFileMonitor before unreffing it
- Do not allocate a 128Mb buffer for each xb_builder_source_ctx_get_bytes()
- Do not error when creating a query if the element doesn’t exist
- Fix a parse failure for a double comment
- Fix various errors or missing annotations in docs
- Make handling of single-result queries more robust
- Support mmap()ing the source file to get bytes
- Support query caching with xb_silo_lookup_query()
- Support UTF-8 for upper-case() and lower-case()
- Use g_str_match_string() for non-ASCII search queries
- Write search tokens into the built silo

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Richard Hughes <richard@hughsie.com> 0.2.1-1
- New upstream release
- Do not assume g_content_type_guess() always returns valid results
- Fix getting translated results in gnome-software
- Update the header location to reflect the new API

* Tue Aug 18 2020 Richard Hughes <richard@hughsie.com> 0.2.0-1
- New upstream release which breaks API and ABI
- Add the missing TEXT:INTE XPath support
- Add variant of xb_silo_query_with_root() avoiding XbNode creation
- Add XB_BUILDER_SOURCE_FLAG_WATCH_DIRECTORY flag
- Allow specifying the node cache behaviour for the query
- Avoid recursion when setting flags if possible
- Avoid using weak pointers when building the silo
- Do not allocate opcodes individually
- Do not show a critical warning for invalid XML
- Do not unconditionally create GTimer objects
- Do not use the node cache when building indexes
- Lazy load more arrays to reduce RSS usage

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 04 2020 Richard Hughes <richard@hughsie.com> 0.1.15-1
- New upstream release
- Add xb_builder_source_add_simple_adapter()
- Allow reversing the query results

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Richard Hughes <richard@hughsie.com> 0.1.14-1
- New upstream release
- Do not use libuuid
- Ignore adaptors added with xb_builder_source_add_converter()

* Thu Oct 17 2019 Richard Hughes <richard@hughsie.com> 0.1.13-1
- New upstream release
- Export xb_silo_query_full()
- Show the XPath that was used in the query in the error message

* Fri Sep 27 2019 Richard Hughes <richard@hughsie.com> 0.1.12-1
- New upstream release
- Add xb_node_transmogrify to allow changing XML format
- Do not escape a single quote with &apos;
- Don't invalidate the silo for a GIO temp file
- Fix up two memory leaks if using libxmlb from an introspected binding

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Richard Hughes <richard@hughsie.com> 0.1.11-1
- New upstream release
- Add xb_node_query_first_full() API
- Rebuild the XbMachine parser to support 'and' and 'or' predicates

* Thu May 16 2019 Richard Hughes <richard@hughsie.com> 0.1.10-1
- New upstream release
- Do not mistake gzipped files as being application/x-zerosize content type
- Fix running the installed tests with no checkout directory

* Tue May 07 2019 Richard Hughes <richard@hughsie.com> 0.1.9-1
- New upstream release
- Correctly implement building a silo with _SINGLE_LANG set

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.1.8-2
- Rebuild with Meson fix for #1699099

* Tue Mar 26 2019 Richard Hughes <richard@hughsie.com> 0.1.8-1
- New upstream release
- Add some installed tests
- Always add all children when importing parent-less XML data

* Fri Mar 08 2019 Richard Hughes <richard@hughsie.com> 0.1.7-1
- New upstream release
- Add XB_BUILDER_COMPILE_FLAG_IGNORE_GUID
- Allow nesting XbBuilderSource content type handlers

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Richard Hughes <richard@hughsie.com> 0.1.6-1
- New upstream release
- Allow controlling how the XbQuery is parsed

* Wed Nov 21 2018 Richard Hughes <richard@hughsie.com> 0.1.5-1
- New upstream release
- Add xb_builder_node_export() for gnome-software
- Ignore calls to xb_silo_query_build_index() with no results
- Lazy load the stemmer when required

* Fri Nov 09 2018 Richard Hughes <richard@hughsie.com> 0.1.4-1
- New upstream release
- Add support for bound variables and indexed strings
- Optionally optimize predicates
- Use INTE:INTE for comparison where available

* Mon Oct 22 2018 Richard Hughes <richard@hughsie.com> 0.1.3-1
- New upstream release
- Add more API for fwupd and gnome-software
- Switch from GPtrArray to XbStack for performance reasons

* Tue Oct 16 2018 Richard Hughes <richard@hughsie.com> 0.1.2-1
- New upstream release
- Add more API for fwupd and gnome-software
- Fix a crash when using xb_builder_node_set_text() in a fixup
- Only run the XbBuilderSourceConverterFunc if the silo needs rebuilding
- Return an error when the XPath predicate has invalid syntax

* Thu Oct 11 2018 Richard Hughes <richard@hughsie.com> 0.1.1-1
- New upstream release
- Add support for more XPath funtions
- Add new API required for gnome-software and fwupd

* Thu Oct 04 2018 Richard Hughes <richard@hughsie.com> 0.1.0-1
- Initial release for Fedora package review
