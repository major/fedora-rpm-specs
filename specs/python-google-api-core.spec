%bcond tests 1

Name:           python-google-api-core
Version:        2.26.0
Epoch:          1
Release:        %autorelease
Summary:        Google API client core library

License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-core
Source0:        %{url}/archive/v%{version}/python-api-core-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  tomcli

%if %{with tests}
# See noxfile.py:
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
%endif

BuildArch:      noarch

%global _description %{expand:
This library is not meant to stand alone. Instead it defines common helpers
used by all Google API clients.}

%description %{_description}


%package -n python3-google-api-core
Summary:        %{summary}

%if %[ %{defined fc43} || %{defined fc42} || %{defined fc41} || %{defined el10} ]
# Historically, we added manual dependencies corresponding to the “grpc” extra.
# There’s no good reason to do that, since packages that need grpcio should be
# depending on google-api-core[grpc], so we stopped doing it as of Fedora 44.
Requires:       python3-google-api-core+grpc = %{epoch}:%{version}-%{release}
%endif

%description -n python3-google-api-core %{_description}


%pyproject_extras_subpkg -n python3-google-api-core async_rest grpc grpcgcp grpcio-gcp


%prep
%autosetup -n python-api-core-%{version} -p1

# Remove lower bounds on the versions of protobuf, proto-plus, and grpcio.  The
# protobuf and grpc packages have proven very difficult to update, and they are
# languishing at old and increasingly-broken versions, but we must work with
# what is available.
for dep in protobuf proto-plus
do
  # Don’t use “lists replace” since there may be multiple copies for different
  # Python versions. Replace the dependency entirely with an unversioned one.
  tomcli set pyproject.toml lists delitem --no-first \
      project.dependencies "^${dep}\b.*"
  tomcli set pyproject.toml append project.dependencies "${dep}"
done
# NOTE(mhayden): All of the tests pass fine with 1.48.3
# which is in rawhide/f38 as of 2023-02-20.
for dep in grpcio grpcio-status
do
  tomcli set pyproject.toml lists delitem --no-first \
      project.optional-dependencies.grpc "^${dep}\b.*"
  tomcli set pyproject.toml append project.optional-dependencies.grpc "${dep}"
done


%generate_buildrequires
%pyproject_buildrequires -x async_rest,grpc,grpcgcp,grpcio-gcp


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l google


%check
%pyproject_check_import
%if %{with tests}
# TODO: Try to determine whether the root cause is within this package and
# report these upstream.
# E           RuntimeError: There is no current event loop in thread 'MainThread'.
k="${k-}${k+ and }not test_from_gapic"
k="${k-}${k+ and }not test_metadata"

# Since 2.15.0:
#
# /usr/lib/python3.14/site-packages/google/protobuf/internal/well_known_types.py:92:
#         in <module>
#     _EPOCH_DATETIME = datetime.utcfromtimestamp(0)
# E   DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated
#         and scheduled for removal in a future version. Use timezone-aware
#         objects to represent datetimes in UTC:
#         datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
#
# ----
#
# /usr/lib/python3.14/site-packages/google/protobuf/descriptor.py:97: in
#         _Deprecated
#     warnings.warn(
# E   DeprecationWarning: Call to deprecated create function FileDescriptor().
#         Note: Create unlinked descriptors is going to go away. Please use
#         get/find descriptors from generated code or query the
#         descriptor_pool.
#
# ----
#
# We are stuck with both of the above until someone can actually update the
# protobuf package.
#
# Additionally, since 2.17.0:
#
# /usr/lib/python3.14/site-packages/proto/datetime_helpers.py:24: in <module>
#     _UTC_EPOCH = datetime.datetime.utcfromtimestamp(0).replace(
#         tzinfo=datetime.timezone.utc)
# E   DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated
#         and scheduled for removal in a future version. Use timezone-aware
#         objects to represent datetimes in UTC:
#         datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
#
# We are stuck with this until someone can actually update the proto-plus
# package.
warningsfilter="${warningsfilter-} -W ignore:datetime:DeprecationWarning"
warningsfilter="${warningsfilter-} -W ignore:Call:DeprecationWarning"

%pytest ${warningsfilter-} -k "${k-}" tests
%endif


%files -n python3-google-api-core -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.rst
%doc SECURITY.md


%changelog
%autochangelog
