%global forgeurl https://github.com/mtth/hdfs

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a lesser substitute.
%bcond doc_pdf 1

Name:           python-hdfs
Version:        2.7.3
Release:        %autorelease
Summary:        API and command line interface for HDFS
%forgemeta
# SPDX
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
# Downstream man pages in groff_man(7) format. These were written for Fedora
# based on the tools’ --help output and should be updated if the command-line
# interface changes.
Source1:        hdfscli.1
Source2:        hdfscli-avro.1

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
#
# Additionally, fastavro (required by some extras metapackages) is not
# available on 32-bit architectures. Excluding these allows us to stop
# conditionalizing those architectures.
ExcludeArch:    %{ix86}

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

%description -n python3-hdfs %{_description}


# We manually write out the python3-hdfs+avro subpackage so that it can contain
# the hdfscli-avro CLI entry point, and so that its summary and description can
# be tweaked to reflect this.  The definition is based on:
#
#   rpm -E '%%pyproject_extras_subpkg -n python3-hdfs avro'
%package -n python3-hdfs+avro
Summary:        Package for python3-hdfs: avro extras

Requires:       python3-hdfs = %{version}-%{release}

%description -n python3-hdfs+avro
This is a package bringing in avro extras requires for python3-hdfs.
It makes sure the dependencies are installed.

It also includes the avro-specific command-line tool, hdfscli-avro.

%pyproject_extras_subpkg -n python3-hdfs dataframe kerberos


%package doc
Summary:    Documentation and examples for %{name}

%description doc %{_description}


%prep
%forgeautosetup -p1

# Remove shebangs from non-script sources. The find-then-modify pattern keeps
# us from discarding mtimes on sources that do not need modification.
find . -type f ! -perm /0111 \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'


%generate_buildrequires
%pyproject_buildrequires -x avro,dataframe,kerberos


%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" sphinx-build -b latex doc _latex -j%{?_smp_build_ncpus}
%make_build -C _latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l hdfs
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 %{SOURCE1} %{SOURCE2}


%check
# Ignore upstream tests - require a hadoop cluster setup
# https://github.com/mtth/hdfs/blob/master/.travis.yml#L10
%pyproject_check_import


%files -n python3-hdfs -f %{pyproject_files}
%{_bindir}/hdfscli
%{_mandir}/man1/hdfscli.1*


%files -n python3-hdfs+avro
%ghost %{python3_sitelib}/*.dist-info

%{_bindir}/hdfscli-avro
%{_mandir}/man1/hdfscli-avro.1*


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
%autochangelog
