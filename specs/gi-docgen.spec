# Sphinx-generated HTML documentation is historically not suitable for
# packaging; see https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for
# discussion. We can generate PDF documentation as a substitute.
#
# In Fedora 42 and later, we can (and in Fedora 43 and later, we do) build the
# HTML documentation but unbundle Doxygen-inserted JavaScript assets from the
# HTML documentation as much as possible, as prescribed in
# https://src.fedoraproject.org/rpms/doxygen/blob/f42/f/README.rpm-packaging.
%bcond doc_pdf %[ %{defined fc41} || %{defined fc42} ]


Name:           gi-docgen
Version:        2025.4
Release:        %autorelease
Summary:        Documentation tool for GObject-based libraries

# Based on the “Copyright and Licensing terms” in README.md, on the contents of
# .reuse/dep5, and on inspection of SPDX headers or other file contents with
# assistance from licensecheck.
#
# The entire source is (Apache-2.0 OR GPL-3.0-or-later) except the following files that are
# packaged or are used to generate packaged files:
#
# (Apache-2.0 OR GPL-3.0-or-later) AND BSD-2-Clause:
#   - gidocgen/mdext.py
#
# MIT:
#   - gidocgen/templates/basic/fzy.js
#   - gidocgen/templates/basic/solarized-{dark,light}.js
#
# CC0-1.0:
#   - gi-docgen.pc.in (from which gi-docgen.pc is generated)
#   - gidocgen/templates/basic/*.png
#   - docs/CODEOWNERS (-doc subpackage)
#   - examples/*.toml (-doc subpackage)
#
# Note that CC0-1.0 is allowed in Fedora for content only; all of the above
# files may reasonably be called content.
#
# Additionally, CC0-1.0 appears in certain sample configuration snippets within
# the following files, which are otherwise (Apache-2.0 OR GPL-3.0-or-later):
#   - docs/project-configuration.rst
#   - docs/tutorial.rst
# On one hand, these are copied from real projects; on the other hand, they are
# very trivial. It’s not obvious whether they should be considered “real”
# CC0-1.0 content or not.
#
# The identifier LGPL-2.1-or-later also appears in a sample configuration
# template in docs/tutorial.rst, but the configuration in question is filled
# with placeholder values and is not copied from a real project, so it’s
# reasonable to consider LGPL-2.1-or-later a placeholder rather than a real
# license as well.
License:        %{shrink:
                (Apache-2.0 OR GPL-3.0-or-later) AND
                BSD-2-Clause AND
                MIT AND
                CC0-1.0
                }
# Additionally, the following sources are under licenses other than (Apache-2.0
# OR GPL-3.0-or-later), but are not packaged in any of the binary RPMs:
#
# CC0-1.0:
#   - .editorconfig (not installed)
#   - .gitlab-ci.yml (not installed)
#   - gi-docgen.doap (not installed)
#   - MANIFEST.in (not installed)
#   - pytest.ini (not installed; test only)
#   - tests/data/config/*.toml (not installed; test only)
#
# CC-BY-SA-3.0:
#   - docs/gi-docgen.{png,svg} (for HTML docs; not currently packaged)
#   - code-of-conduct.md (not installed)
#
# OFL-1.1:
#   - gidocgen/templates/basic/*.{woff,woff2} (removed in prep)
#
# GPL-2.0-or-later:
#   - tests/data/gir/{Utility-1.0,Regress-1.0}.gir (not installed; test only)
#
# LGPL-2.0-or-later:
#   - tests/data/gir/{GLib,GObject,Gio}-2.0.gir (not installed; test only)
#
# LGPL-2.0-or-later OR MPL-1.1:
#   - tests/data/gir/cairo-1.0.gir (not installed; test only)
SourceLicense:  %{shrink:
                %{license} AND
                CC-BY-SA-3.0 AND
                GPL-2.0-or-later AND
                LGPL-2.0-or-later AND
                (LGPL-2.0-or-later OR MPL-1.1) AND
                OFL-1.1
                }
URL:            https://gitlab.gnome.org/GNOME/gi-docgen
Source:         %{url}/-/archive/%{version}/gi-docgen-%{version}.tar.bz2

# We are prohibited from bundling fonts, and we are prohibited from shipping
# fonts in web font formats; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/FontsPolicy/#_web_fonts.
#
# Since upstream uses *only* web fonts, we need a patch. We haven’t offered it
# upstream since upstream has no reason NOT to use web fonts.
#
# This patch removes all references to WOFF/WOFF2 font files (which we still
# must remove in %%prep) and ensures the CSS correctly references corresponding
# or stand-in local system fonts.
Patch:          gi-docgen-2022.2-no-web-fonts.patch

BuildSystem:            pyproject
BuildOption(install):   gidocgen

BuildArch:      noarch

BuildRequires:  python3dist(pytest)

# Documentation
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%if %{with doc_pdf}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

# Unbundling fonts:
BuildRequires:  font(redhatdisplay)
BuildRequires:  font(redhatdisplayblack)
BuildRequires:  font(redhatdisplaymedium)
BuildRequires:  font(redhattext)
BuildRequires:  font(redhattextmedium)
%if 0%{?rhel} >= 10
BuildRequires:  redhat-mono-vf-fonts
%else
BuildRequires:  font(sourcecodepro)
BuildRequires:  font(sourcecodeprosemibold)
%endif

# Unbundling fonts:
Requires:       gi-docgen-fonts = %{version}-%{release}

# Trivial fork of https://github.com/jhawthorn/fzy.js (looks like it was
# basically just wrapped in an IIFE). Given that modification, it’s not clear
# how we could unbundle it, either downstream or with some kind of upstream
# support.
#
# It’s not clear what version was used for the fork.
Provides:       bundled(js-fzy)

%description
GI-DocGen is a document generator for GObject-based libraries. GObject is the
base type system of the GNOME project. GI-Docgen reuses the introspection data
generated by GObject-based libraries to generate the API reference of these
libraries, as well as other ancillary documentation.

GI-DocGen is not a general purpose documentation tool for C libraries.

While GI-DocGen can be used to generate API references for most GObject/C
libraries that expose introspection data, its main goal is to generate the
reference for GTK and its immediate dependencies. Any and all attempts at
making this tool more generic, or to cover more use cases, will be weighted
heavily against its primary goal.

GI-DocGen is still in development. The recommended use of GI-DocGen is to add
it as a sub-project to your Meson build system, and vendor it when releasing
dist archives.

You should not depend on a system-wide installation until GI-DocGen is declared
stable.


%package fonts
Summary:        Metapackage providing fonts for gi-docgen output
# Really, there is nothing copyrightable in this metapackage, so we give it the
# overall license of the project.
License:        Apache-2.0 OR GPL-3.0-or-later

Requires:       font(redhatdisplay)
Requires:       font(redhatdisplayblack)
Requires:       font(redhatdisplaymedium)
Requires:       font(redhattext)
Requires:       font(redhattextmedium)
%if 0%{?rhel} >= 10
Requires:       redhat-mono-vf-fonts
%else
Requires:       font(sourcecodepro)
Requires:       font(sourcecodeprosemibold)
%endif

%description fonts
Because web fonts from upstream are not bundled in the gi-docgen package,
documentation packages generated with gi-docgen must depend on this metapackage
to ensure the proper system fonts are present.


%package doc
Summary:        Documentation for gi-docgen
License:        (Apache-2.0 OR GPL-3.0-or-later) AND CC0-1.0

%description doc
Documentation for gi-docgen.


%prep -a
# Remove all bundled fonts. See gi-docgen-*-no-web-fonts.patch.
find . -type f \( -name '*.woff' -o -name '*.woff2' \) -print -delete


%build -a
%if %{with doc_pdf}
sphinx-build -b latex -j%{?_smp_build_ncpus} docs %{_vpath_builddir}/_latex
%make_build -C %{_vpath_builddir}/_latex LATEXMKOPTS='-quiet'
%else
sphinx-build -b html -j%{?_smp_build_ncpus} docs %{_vpath_builddir}/_html
# Do not ship hashes and caches for incremental rebuilds.
rm -rv %{_vpath_builddir}/_html/{.buildinfo,.doctrees}
%endif


%install -a
install -t '%{buildroot}%{_pkgdocdir}' -D -m 0644 -p \
    CHANGES.md \
    CONTRIBUTING.md \
    docs/CODEOWNERS \
    README.md
%if %{with doc_pdf}
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 \
    '%{_vpath_builddir}/_latex/gi-docgen.pdf'
%else
cp -rp '%{_vpath_builddir}/_html' '%{buildroot}%{_pkgdocdir}/html'
%endif
cp -rp examples '%{buildroot}%{_pkgdocdir}/'


%check -a
%pytest


%files -f %{pyproject_files}
%license LICENSES/ .reuse/dep5

%{_bindir}/gi-docgen
%{_mandir}/man1/gi-docgen.1*
# Normally, this would go in a -devel package, but there is little point in
# providing a -devel package for *just* the .pc file when there are no
# libraries or headers.
%{_datadir}/pkgconfig/gi-docgen.pc


%files fonts
# Empty; this is a metapackage


%files doc
%license LICENSES/ .reuse/dep5
%doc %{_pkgdocdir}/


%changelog
%autochangelog
