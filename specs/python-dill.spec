%bcond_without check

Name: python-dill
Version: 0.4.0
Release: %autorelease
Summary: Serialize all of Python

License: BSD-3-Clause

URL: https://github.com/uqfoundation/dill
Source: %{pypi_source dill}

# Pickle _contextvars.Context objects, for threads in Python 3.14+
Patch: https://github.com/uqfoundation/dill/pull/717.patch

BuildArch: noarch

BuildRequires: python3-devel
# the test script calls 'python', this is easier than patching it
BuildRequires: python-unversioned-command

%global _description %{expand:
Dill extends Python's pickle module for serializing and de-serializing Python
objects to the majority of the built-in Python types. Serialization is the
process of converting an object to a byte stream, and the inverse of which is
converting a byte stream back to a Python object hierarchy.

Dill provides the user the same interface as the pickle module, and also
includes some additional features. In addition to pickling Python objects, dill
provides the ability to save the state of an interpreter session in a single
command. Hence, it would be feasible to save an interpreter session, close the
interpreter, ship the pickled file to another computer, open a new interpreter,
unpickle the session and thus continue from the 'saved' state of the original
interpreter session.

Dill can be used to store Python objects to a file, but the primary usage is to
send Python objects across the network as a byte stream. dill is quite
flexible, and allows arbitrary user defined classes and functions to be
serialized. Thus dill is not intended to be secure against erroneously or
maliciously constructed data. It is left to the user to decide whether the data
they unpickle is from a trustworthy source.

dill is part of pathos, a Python framework for heterogeneous computing.}

%description %{_description}


%package -n python3-dill
Summary:  %{summary}

%description -n python3-dill %{_description}


# The graph extra needs objgraph>=1.7.2; python-objgraph is not packaged
# The profile extra needs gprof2dot>=2022.7.29; python-gprof2dot is not packaged
%pyproject_extras_subpkg -n python3-dill readline


%prep
%autosetup -p1 -n dill-%{version}


%generate_buildrequires
%pyproject_buildrequires -x readline


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l dill

# We do not want to package these command-line tools, and we lack the necessary
# dependencies for the corresponding extras anyway.
rm %{buildroot}%{_bindir}/get_objgraph %{buildroot}%{_bindir}/get_gprof

# Remove shebangs from (installed) non-script sources. The find-then-modify
# pattern preserves mtimes on sources that did not need to be modified.
find '%{buildroot}%{python3_sitelib}/dill' -type f -name '*.py' ! -perm /0111 \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'


# Skip offending tests to allow other packages to rebuiltd with py313
# https://bugzilla.redhat.com/show_bug.cgi?id=2264225
%check
%if %{with check}
%{py3_test_envvars} %{python3} dill/tests/__main__.py
%endif
%pyproject_check_import -t



%files -n python3-dill -f %{pyproject_files}
%doc README.md
%{_bindir}/undill


%changelog
%autochangelog
