# The source tarball on PyPI contains generated sources. We are not required to
# produce the generated sources from scratch in the build process, but it is
# nice that we can do so.
#
# See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/what-can-be-packaged/#_pregenerated_code:
#
#   It is required that the original source files from which the code was
#   generated be included in the source package. Generally these files are part
#   of the source archive supplied by upstream, but it may be necessary to
#   fetch those files from an upstream source repository and include them in
#   the source package as separate Source: entries.
#
# The “true” source is, as noted in the description, grpc, along with release
# tarballs corresponding to third-party git submodules pulled in by grpc. Note
# that we do not treat these additional sources as bundled dependencies, since
# (provably) only the .proto files are used. Additionally, where possible, we
# depend on other packages that already provide the necessary generated Python
# files.
%global grpc_url https://github.com/grpc/grpc
%global grpc_tag v1.40.0
#global grpc_commit xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#global grpc_snapdate YYYYMMDD

# Check tools/distrib/python/xds_protos/build.py in the grpc tarball for a list
# of these third-party submodules, and
# https://github.com/grpc/grpc/tree/v%%{grpc_version}/third_party for the
# commit hashes used in the grpc release.
#
# This will probably never be separately packaged in Fedora, since upstream can
# only build with Bazel (and Bazel is such a mess of bundled dependencies that
# it is unlikely to every be successfully packaged under the Fedora packaging
# guidelines.
%global envoy_api_commit df3b1ab2773147f292c4f175f790c35448328161
#
# Upstream also only builds with Bazel:
%global udpa_proto_commit 6414d713912e988471d192940b62bf552b11793a
#
%global googleapis_commit 2f9af297c84c55c8b871ba4495e01ade42476c92
#
%global protoc_gen_validate_commit 59da36e59fef2267fc2b1849a05159e3ecdf24f3
#
# We can’t omit these two sources (and patch the corresponding proto
# compilations out of build.py) because the original .proto files are
# referenced from the envoy proto files, which we *do* need to compile.
#
%global opencensus_proto_commit 4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89
%global opentelemetry_proto_commit 60fa8754d890b5c55949a8c68dcfd7ab5c2395df

# These minimum versions help keep track of what unbundled versions are needed.
# Since we are able to completely unbundle the generated proto wrappers for
# opencensus and opentelemetry, the version bounds are not extremely strict.
%global opencensus_proto_min_version 0.3
%global opentelemetry_proto_min_version 1.13
# It is unfortunate but unavoidable that this package must stuff additional
# files inside the unbundled googlapis-common-protos directories. This means
# than any update to python-googleapis-common-protos could potentially require
# python-xds-protos to be rebuilt. We therefore use an exact-version
# dependency.
%global googleapis_common_protos_version 1.58

Name:           python-xds-protos
Version:        0.0.11%{?grpc_commit:^%{grpc_snapdate}git%{grpc_commit}}
Release:        %autorelease -b 9
Summary:        ProtoBuf generated Python files for xDS protos

# The entire source (after removing unused non-.proto files in %%prep) is Apache-2.0, except:
#
# - The following .proto files are BSD-3-Clause. However, they are for
#   benchmarks and are not used to generate the proto bindings in this package,
#   so do not affect the license of the binary RPMs.
#
#   third_party/upb/benchmarks/descriptor.proto
#   third_party/upb/benchmarks/descriptor_sv.proto

License:        Apache-2.0
URL:            https://pypi.org/project/xds-protos
%global grpc_version %(echo '%{grpc_tag}' | sed -r 's/^v//')
Source0:        %{grpc_url}/archive/%{grpc_tag}/grpc-%{grpc_version}.tar.gz

%global envoy_api_url https://github.com/envoyproxy/data-plane-api
%global udpa_proto_url https://github.com/cncf/udpa
%global googleapis_url https://github.com/googleapis/googleapis
%global protoc_gen_validate_url https://github.com/envoyproxy/protoc-gen-validate
%global opencensus_proto_url https://github.com/census-instrumentation/opencensus-proto
%global opentelemetry_proto_url https://github.com/open-telemetry/opentelemetry-proto

%global envoy_api_dir data-plane-api-%{envoy_api_commit}
%global udpa_proto_dir udpa-%{udpa_proto_commit}
%global googleapis_dir googleapis-%{googleapis_commit}
%global protoc_gen_validate_dir protoc-gen-validate-%{protoc_gen_validate_commit}
%global opencensus_proto_dir opencensus-proto-%{opencensus_proto_commit}
%global opentelemetry_proto_dir opentelemetry-proto-%{opentelemetry_proto_commit}

Source1:        %{envoy_api_url}/archive/%{envoy_api_commit}/%{envoy_api_dir}.tar.gz
Source2:        %{udpa_proto_url}/archive/%{udpa_proto_commit}/%{udpa_proto_dir}.tar.gz
Source3:        %{googleapis_url}/archive/%{googleapis_commit}/%{googleapis_dir}.tar.gz
Source4:        %{protoc_gen_validate_url}/archive/%{protoc_gen_validate_commit}/%{protoc_gen_validate_dir}.tar.gz
Source5:        %{opencensus_proto_url}/archive/%{opencensus_proto_commit}/%{opencensus_proto_dir}.tar.gz
Source6:        %{opentelemetry_proto_url}/archive/%{opentelemetry_proto_commit}/%{opentelemetry_proto_dir}.tar.gz

# This Python script helps us handle cases where we have to “overlay”
# additional files on top of our dependencies by removing files in this package
# that are provided by dependencies.
Source100:      unbundle_dependencies
# This Python script helps us handle cases where we have to “overlay”
# additional files on top of our dependencies by re-combining this package and
# its dependencies in a single sitelib directory for testing.
Source101:      overlay_dependencies
# This Python script helps verify we have no file conflicts with our
# dependencies at the end.
Source102:      check_conflicts

BuildArch:      noarch

BuildRequires:  python3-devel

# Note that grpc has a circular dependency on this package (xds-protos). The
# bootstrapping is handled in the grpc package: it is possible to build
# everything except (as of grpc 1.40) the grpcio-admin Python package and the
# Python CSDS API package without xds-protos. This is sufficient, as xds-protos
# depends only on grpcio and grpcio-tools.
BuildRequires:  python3dist(grpcio-tools)

# Some of the files in this package duplicate (conflict with) those in
# googleapis-common-protos. We package only the “extra” files.
BuildRequires:  python3dist(googleapis-common-protos) == %{googleapis_common_protos_version}
# Everything this package would install under the opencensus package is
# already provided by opencensus-proto.
BuildRequires:  python3dist(opencensus-proto) >= %{opencensus_proto_min_version}
# Everything this package would install under the opentelemetry package is
# already provided by opentelemetry-proto.
BuildRequires:  python3dist(opentelemetry-proto) >= %{opentelemetry_proto_min_version}

# Working directory, relative to the extracted source distribution, from which
# the build.py and setup.py scripts should be launched. This is a convenience
# macro specific to this spec file.
%global py_cwd tools/distrib/python/xds_protos

%global common_description %{expand:
Package “xds-protos” is a collection of ProtoBuf generated Python files for xDS
protos (or the data-plane-api, https://github.com/envoyproxy/data-plane-api).
You can find the source code of this project in https://github.com/grpc/grpc.
For any question or suggestion, please post to
https://github.com/grpc/grpc/issues.

Each generated Python file can be imported according to their proto package.
For example, if we are trying to import a proto located at
“envoy/service/status/v3/csds.proto”, whose proto package is
“package envoy.service.status.v3”, then we can import it as:

  # Import the message definitions
  from envoy.service.status.v3 import csds_pb2
  # Import the gRPC service and stub
  from envoy.service.status.v3 import csds_pb2_grpc}

%description %{common_description}


%package -n     python3-xds-protos
Summary:        %{summary}

Requires:       python3dist(googleapis-common-protos) == %{googleapis_common_protos_version}
Requires:       python3dist(opencensus-proto) >= %{opencensus_proto_min_version}
Requires:       python3dist(opentelemetry-proto) >= %{opentelemetry_proto_min_version}

%description -n python3-xds-protos %{common_description}


%prep
%autosetup -n grpc-%{grpc_version}

# Extract the source tarballs corresponding to the necessary git submodules.
%setup -q -T -D -b 1 -n grpc-%{grpc_version}
%setup -q -T -D -b 2 -n grpc-%{grpc_version}
%setup -q -T -D -b 3 -n grpc-%{grpc_version}
%setup -q -T -D -b 4 -n grpc-%{grpc_version}
%setup -q -T -D -b 5 -n grpc-%{grpc_version}
%setup -q -T -D -b 6 -n grpc-%{grpc_version}

{
  awk '$1 ~ /^(#|$)/ { next }; 1' <<'EOF'
../%{envoy_api_dir}/ third_party/envoy-api/
../%{udpa_proto_dir}/ third_party/udpa/
../%{googleapis_dir}/ third_party/googleapis/
../%{protoc_gen_validate_dir}/ third_party/protoc-gen-validate/
../%{opencensus_proto_dir}/ third_party/opencensus-proto/
../%{opentelemetry_proto_dir}/ third_party/opentelemetry/
EOF
} | while read -r fromdir todir
do
  # Remove the empty directory corresponding to the git submodule
  rm -rvf "${todir}"
  # Move the extracted source, to the location where the git submodule would be
  # in a git checkout that included it.
  mv "${fromdir}" "${todir}"
  # Later in %%prep, we will remove all of the extracted source except the
  # .proto files.
done

# Remove everything from the source tree that we don’t need, to prove that none
# of it is bundled.

# First, remove everything at the top level except the LICENSE file,
# third_party/ (which contains necessary .proto files), and tools/ (which is a
# parent directory of the actual source for this package).
find '.' -mindepth 1 -maxdepth 1 \
    ! \( -name 'LICENSE' -o -name 'third_party' -o -name 'tools' \) \
     -print -execdir rm -rf '{}' '+'
# Next, remove all files in third_party/ that are NOT .proto files; some but
# not all of them are bundled dependencies in grpc. (Bundled dependencies would
# not be used in this build anyway, but removing them proves this.) All known
# bundled dependencies in the grpc release are in third_party/.
#
# Note that all of the extracted source tarballs corresponding to git
# submodules were moved here, so nothing remains of them but .proto files.
find 'third_party/' -type f ! -name '*.proto' -print -delete
# Next, remove everything in tools/ except tools/distrib/ (which is a parent
# directory of the actual source for this package).
find 'tools/' -mindepth 1 -maxdepth 1 ! -name 'distrib' \
    -print -execdir rm -rf '{}' '+'
# Again for tools/distrib except tools/distrib/python
find 'tools/distrib' -mindepth 1 -maxdepth 1 ! -name 'python' \
    -print -execdir rm -rf '{}' '+'
# Finally, again for tools/distrib/python except
# tools/distrib/python/xds_protos
find 'tools/distrib/python' -mindepth 1 -maxdepth 1 ! -name 'xds_protos' \
    -print -execdir rm -rf '{}' '+'


%generate_buildrequires
cd %{py_cwd}
%pyproject_buildrequires


%build
cd %{py_cwd}
%{python3} build.py
%pyproject_wheel


%install
cd %{py_cwd}
%pyproject_install
# We meddle with the installed files so much that %%pyproject_save_files is not
# useful.

# Both build.py and generated_file_import_test.py get installed, even though
# upstream attempted to exclude them in setup.py. Additionally, setup.py gets
# installed (inside the package). All of this is wrong.
for pyfile in build setup generated_file_import_test
do
  rm -vf "%{buildroot}%{python3_sitelib}/${pyfile}.py"
done

# Remove the files that conflict with other packages in the distribution, which
# we have added as dependencies.
%{python3} '%{SOURCE100}' \
    '%{buildroot}%{python3_sitelib}' \
    '%{python3_sitelib}'


%check
echo "== Checking for file conflicts with dependencies =="
%{python3} '%{SOURCE102}' \
    '%{buildroot}%{python3_sitelib}' \
    '%{python3_sitelib}'

# To reliably “smoke-test” imports, we must re-combine the installed package
# with the unbundled dependencies that provide some of the imports, as would be
# the case once the resulting RPM is installed—at least in cases where they are
# “mixed” under the same namespace package.
#
# (We don’t need to copy anything for opencensus or opentelemetry, because this
# package installs nothing additional under those namespaces, so importing from
# the buildroot will always work fine.)
dest="${PWD}/testlib"
%{python3} '%{SOURCE101}' \
    '%{buildroot}%{python3_sitelib}' \
    "${dest}" \
    '%{python3_sitelib}/google' \
    '%{python3_sitelib}/opencensus' \
    '%{python3_sitelib}/opentelemetry'
if [ -d '%{python3_sitearch}/google/protobuf' ]
then
  ln -s '%{python3_sitearch}/google/protobuf' "${dest}/google/protobuf"
fi
find '%{python3_sitearch}' '%{python3_sitelib}' \
    -maxdepth 1 -mindepth 1 |
  while read -r dir
  do
    mod="$(basename "${dir}")"
    if [ ! -e "${dest}/${mod}" ]
    then
      ln -s "${dir}" "${dest}/${mod}"
    fi
  done
PYTHONPATH="${PWD}/testlib" PYTHONDONTWRITEBYTECODE=1 \
    %{python3} -S < %{py_cwd}/generated_file_import_test.py


%files -n python3-xds-protos
%license LICENSE

%{python3_sitelib}/envoy/

# Commented-out directories are owned (or co-owned as namespace package
# directories) by python3dist(googleapis-common-protos); since we depend on it,
# we do not need to (co-)own them.
#%%dir %%{python3_sitelib}/google/
#%%dir %%{python3_sitelib}/google/api/
%{python3_sitelib}/google/api/expr/
%{python3_sitelib}/google/api/servicecontrol/
%{python3_sitelib}/google/api/servicemanagement/
%{python3_sitelib}/google/api/serviceusage/
#%%dir %%{python3_sitelib}/google/logging/
#%%dir %%{python3_sitelib}/google/logging/type/
%{python3_sitelib}/google/logging/v2/
#%%dir %%{python3_sitelib}/google/longrunning/
#%%dir %%{python3_sitelib}/google/rpc/
#%%dir %%{python3_sitelib}/google/type/

# Commented-out directories are owned (or co-owned as namespace package
# directories) by python3dist(opencensus-proto); since we depend on it,
# we do not need to (co-)own them.
#%%dir %%{python3_sitelib}/opencensus/
#%%{python3_sitelib}/opencensus/proto/

# Commented-out directories are owned (or co-owned as namespace package
# directories) by python3dist(opentelemetry-proto); since we depend on it,
# we do not need to (co-)own them.
#%%dir %%{python3_sitelib}/opentelemetry
#%%{python3_sitelib}/opentelemetry/proto
# Dropped from python-opentelemetry in v1.15, so it now comes from this
# package:
%{python3_sitelib}/opentelemetry/proto/metrics/experimental/

# This is a namespace package; another package could (but probably will not)
# co-own the directory.
%{python3_sitelib}/udpa/

%{python3_sitelib}/validate/

%{python3_sitelib}/xds/

# Note that there is no importable package or module named xds_protos!
%{python3_sitelib}/xds_protos-%(echo '%{version}' | cut -d '^' -f 1).dist-info/


%changelog
%autochangelog
