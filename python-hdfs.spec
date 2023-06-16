# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a lesser substitute.
%bcond_without doc_pdf

Name:           python-hdfs
Version:        2.6.0
Release:        6%{?dist}
Summary:        API and command line interface for HDFS

License:        MIT
URL:            https://github.com/mtth/hdfs
Source0:        %{url}/archive/%{version}/hdfs-%{version}.tar.gz
# Downstream man pages in groff_man(7) format. These were written for Fedora
# based on the tools’ --help output and should be updated if the command-line
# interface changes.
Source1:        hdfscli.1
Source2:        hdfscli-avro.1

# Use unittest.mock where available
# https://github.com/mtth/hdfs/pull/177
Patch0:         https://github.com/mtth/hdfs/pull/177.patch

# The base package is arched because extras metapackages requiring fastavro are
# not available on 32-bit architectures
# (https://bugzilla.redhat.com/show_bug.cgi?id=1943932).
%ifnarch %{arm32} %{ix86}
%global fastavro_arch 1
%endif
# Of the binary RPMs, only the conditionally-enabled extras metapackages
# python3-hdfs+avro and python3-hdfs+dataframe are arched.
#
# Since there is no compiled code, there are no debugging symbols.
%global debug_package %{nil}

BuildRequires:  python3-devel

# Extra dependencies for documentation
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global _description %{expand:
%{summary}.

Features:

• Python bindings for the WebHDFS (and HttpFS) API, supporting both secure and
  insecure clusters.
• Command line interface to transfer files and start an interactive client
  shell, with aliases for convenient namenode URL caching.
• Additional functionality through optional extensions:
  ○ avro, to read and write Avro files directly from HDFS.
  ○ dataframe, to load and save Pandas dataframes.
  ○ kerberos, to support Kerberos authenticated clusters.}

%description %{_description}


%package -n python3-hdfs
Summary:        %{summary}

BuildArch:      noarch

%description -n python3-hdfs %{_description}


%package doc
Summary:    Documentation and examples for %{name}

BuildArch:      noarch

%description doc %{_description}


%prep
%autosetup -n hdfs-%{version} -p1

# Remove shebangs from non-script sources. The find-then-modify pattern keeps
# us from discarding mtimes on sources that do not need modification.
find . -type f ! -perm /0111 \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'

cp -p '%{SOURCE1}' %{?fastavro_arch:'%{SOURCE2}'} .


%generate_buildrequires
%pyproject_buildrequires -x kerberos%{?fastavro_arch:,avro,dataframe}


# We manually write out the python3-hdfs+kerberos metapackage so that it (like
# python3-hdfs) can be noarch even though the base package is arched. The
# definition is based on:
#
#   rpm -E '%%pyproject_extras_subpkg -n python3-hdfs kerberos
%package -n python3-hdfs+kerberos
Summary:        Metapackage for python3-hdfs: kerberos extras

BuildArch:      noarch

Requires:       python3-hdfs = %{version}-%{release}

%description -n python3-hdfs+kerberos
This is a metapackage bringing in kerberos extras requires for python3-hdfs.
It makes sure the dependencies are installed.

%files -n python3-hdfs+kerberos
%ghost %{python3_sitelib}/*.dist-info


%if 0%{?fastavro_arch}

# Note that this subpackage is arched because it is not available on 32-bit
# architectures.
#
# We manually write out the python3-hdfs+avro subpackage so that it can contain
# the hdfscli-avro CLI entry point, and so that its summary and description can
# be tweaked to reflect this.  The definition is based on:
#
#   rpm -E '%%pyproject_extras_subpkg -n python3-hdfs avro
%package -n python3-hdfs+avro
Summary:        Package for python3-hdfs: avro extras

Requires:       python3-hdfs = %{version}-%{release}

%description -n python3-hdfs+avro
This is a package bringing in avro extras requires for python3-hdfs.
It makes sure the dependencies are installed.

It also includes the avro-specific command-line tool, hdfscli-avro.

%files -n python3-hdfs+avro
%ghost %{python3_sitelib}/*.dist-info

%{_bindir}/hdfscli-avro
%{_mandir}/man1/hdfscli-avro.1*


# Note that this metapackage is arched because it is not available on 32-bit
# architectures.
%pyproject_extras_subpkg -n python3-hdfs dataframe

%endif


%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" sphinx-build -b latex doc _latex %{?_smp_mflags}
%make_build -C _latex
%endif


%install
%pyproject_install
%pyproject_save_files hdfs
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    hdfscli.1 %{?fastavro_arch:hdfscli-avro.1}


%check
# Ignore upstream tests - require a hadoop cluster setup
# https://github.com/mtth/hdfs/blob/master/.travis.yml#L10
%{pyproject_check_import \
    %{?!fastavro_arch:-e hdfs.ext.avro -e hdfs.ext.dataframe}}


%files -n python3-hdfs -f %{pyproject_files}
# pyproject-rpm-macros handles the license file; verify with rpm -qL -p …
%{_bindir}/hdfscli
%{_mandir}/man1/hdfscli.1*
# This is packaged in python3-hdfs+avro on 64-bit architectures; it is not
# packaged at all on 32-bit architectures.
%exclude %{_bindir}/hdfscli-avro


%files doc
%license LICENSE
%doc AUTHORS
%doc CHANGES
%doc README.md
%if %{with doc_pdf}
%doc _latex/hdfs.pdf
%endif
%doc examples


%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.6.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.6.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.0-1
- Update to 2.6.0 (close RHBZ#2020978)

* Fri Oct 29 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.8-12
- Use the new %%pyproject_check_import macro

* Wed Oct 27 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.8-11
- Fix a typo in a comment in the spec file

* Sun Oct 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.8-10
- Fully modernize the packaging
- Switch to “new guidelines” / pyproject-rpm-macros
- Drop conditionals for Python 2 on obsolete Fedora releases
- Rely on Python dependency generator (no manual Requires)
- Build PDF instead of HTML documentation due to guideline issues
- Drop dependencies on deprecated nose and mock
- Properly handle extras metapackages and dependency on unported
  python-fastavro for 32-bit architectures; move the hdfscli-avro entry point
  into the new python3-hdfs+avro package
- Add man pages for command-line tools

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.5.8-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.8-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.8-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.8-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.5.8-1
- Update to new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.5.6-1
- New upstream version

* Wed Jun 12 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.5.4-1
- New upstream version

* Mon May 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.5.2-2
- Add buildrequire
- Fix readme extension

* Mon May 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.5.2-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-7
- Disable py2 on F30+
- Use py3 sphinx for document generation

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-5
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-2
- Fix doc generation
- Fix summary macro
- List binary files

* Mon Jan 15 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.0-1
- Initial build
