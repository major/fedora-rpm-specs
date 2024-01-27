%global _description %{expand:
The LinuxDoc library contains Sphinx-doc extensions and command line tools to
extract documentation from C/C++ source file comments. Even if this project
started in context of the Linux-Kernel documentation, you can use these
extensions in common Sphinx-doc projects.}

Name:           python-linuxdoc
Version:        20231020
Release:        %{autorelease}
Summary:        Sphinx-doc extensions for sophisticated C developer


License:        AGPL-3.0-or-later
URL:            https://return42.github.io/linuxdoc/
Source0:        %{pypi_source linuxdoc}

BuildArch:      noarch

%description %_description

%package -n python3-linuxdoc
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  help2man

%description -n python3-linuxdoc %_description

%prep
%autosetup -n linuxdoc-%{version}

# nothing here, empty package that gets installed in %%{python3_sitelib}
rm -rf tests

# remove shebangs
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install

# generate man pages
# must be done here because binaries must be installed
for binfile in "linuxdoc.autodoc" "linuxdoc.rest" "linuxdoc.grepdoc" "linuxdoc.lintdoc" "kernel-autodoc" "kernel-doc" "kernel-grepdoc" "kernel-lintdoc"
do
    ls -lash "$RPM_BUILD_ROOT/%{_bindir}/${binfile}"
    help2man -N --version-string %{version} -h -h --no-discard-stderr "$RPM_BUILD_ROOT/%{_bindir}/${binfile}" > "${binfile}.1"
done

install -p -m 0644 -D -t "$RPM_BUILD_ROOT/%{_mandir}/man1/"  *.1

%pyproject_save_files linuxdoc

%check
# exclude sphinx < 3.0 bits, we don't have it in Fedora
%pyproject_check_import linuxdoc -e *cdomainv2*

%files -n python3-linuxdoc -f %{pyproject_files}
%doc README.rst
%{_bindir}/linuxdoc.autodoc
%{_bindir}/linuxdoc.rest
%{_bindir}/linuxdoc.grepdoc
%{_bindir}/linuxdoc.lintdoc
%{_bindir}/kernel-autodoc
%{_bindir}/kernel-doc
%{_bindir}/kernel-grepdoc
%{_bindir}/kernel-lintdoc
%{_mandir}/man1/linuxdoc.*
%{_mandir}/man1/kernel-*


%changelog
%autochangelog
