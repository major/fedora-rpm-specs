# Generated by go2rpm 1
%bcond_without check
%bcond_without bootstrap
%global debug_package %{nil}


# https://github.com/google/go-cloud
%global goipath         gocloud.dev
%global forgeurl        https://github.com/google/go-cloud
Version:                0.24.0
Epoch:                  1

%gometa

%global goipaths0       gocloud.dev
%global goipathsex0     gocloud.dev/secrets/hashivault

%if %{without bootstrap}
%global goipaths1       gocloud.dev/secrets/hashivault
%endif

%global common_description %{expand:
The Go Cloud Development Kit (Go CDK) allows Go application developers to
seamlessly deploy cloud applications on any combination of cloud providers. It
does this by providing stable, idiomatic interfaces for common uses like storage
and databases. Think database/sql for cloud products.}

%global golicenses      LICENSE
%global godocs          AUTHORS CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        CONTRIBUTORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Library and tools for open cloud development in Go

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
# To use etcd 3.5.0 and newer
Patch0:         0001-Fix-to-use-latest-etcd.patch
Patch1:         0002-Fix-bool.patch

BuildRequires:  golang(cloud.google.com/go/compute/metadata)
BuildRequires:  golang(cloud.google.com/go/firestore/apiv1)
BuildRequires:  golang(cloud.google.com/go/iam/credentials/apiv1)
BuildRequires:  golang(cloud.google.com/go/kms/apiv1)
BuildRequires:  golang(cloud.google.com/go/pubsub/apiv1)
BuildRequires:  golang(cloud.google.com/go/secretmanager/apiv1)
BuildRequires:  golang(cloud.google.com/go/storage)
BuildRequires:  golang(contrib.go.opencensus.io/exporter/aws)
BuildRequires:  golang(contrib.go.opencensus.io/exporter/stackdriver)
BuildRequires:  golang(contrib.go.opencensus.io/exporter/stackdriver/monitoredresource)
BuildRequires:  golang(contrib.go.opencensus.io/integrations/ocsql)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/kms)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/secretsmanager)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/ssm)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/ssm/types)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/client)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/dynamodb)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/dynamodb/expression)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/kms)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/secretsmanager)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/sns)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/sqs)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/ssm)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/xray)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/xray/xrayiface)
BuildRequires:  golang(github.com/aws/smithy-go)
BuildRequires:  golang(github.com/Azure/azure-amqp-common-go/v3)
BuildRequires:  golang(github.com/Azure/azure-amqp-common-go/v3/uuid)
BuildRequires:  golang(github.com/Azure/azure-pipeline-go/pipeline)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go/services/keyvault/v7.0/keyvault)
BuildRequires:  golang(github.com/Azure/azure-service-bus-go)
BuildRequires:  golang(github.com/Azure/azure-storage-blob-go/azblob)
BuildRequires:  golang(github.com/Azure/go-amqp)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure/auth)
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/google/go-replayers/grpcreplay)
BuildRequires:  golang(github.com/google/go-replayers/httpreplay)
BuildRequires:  golang(github.com/google/go-replayers/httpreplay/google)
BuildRequires:  golang(github.com/google/subcommands)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/google/wire)
BuildRequires:  golang(github.com/googleapis/gax-go/v2)
BuildRequires:  golang(github.com/GoogleCloudPlatform/cloudsql-proxy/proxy/certs)
BuildRequires:  golang(github.com/GoogleCloudPlatform/cloudsql-proxy/proxy/proxy)
BuildRequires:  golang(github.com/gorilla/mux)
%if %{without bootstrap}
BuildRequires:  golang(github.com/hashicorp/vault/api)
%endif
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/nats-io/nats.go)
BuildRequires:  golang(github.com/Shopify/sarama)
BuildRequires:  golang(github.com/streadway/amqp)
BuildRequires:  golang(go.etcd.io/etcd/client/v3)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/v3rpc/rpctypes)
BuildRequires:  golang(go.mongodb.org/mongo-driver/bson)
BuildRequires:  golang(go.mongodb.org/mongo-driver/bson/primitive)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo/options)
BuildRequires:  golang(go.opencensus.io/plugin/ocgrpc)
BuildRequires:  golang(go.opencensus.io/plugin/ochttp)
BuildRequires:  golang(go.opencensus.io/stats)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/tag)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(golang.org/x/xerrors)
BuildRequires:  golang(google.golang.org/api/googleapi)
BuildRequires:  golang(google.golang.org/api/iterator)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/kms/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/runtimeconfig/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/secretmanager/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/firestore/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/iam/credentials/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/pubsub/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/type/latlng)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/credentials/oauth)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gopkg.in/pipe.v2)

%if %{with check}
# Tests
BuildRequires:  golang(cloud.google.com/go/firestore)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/dynamodb/dynamodbattribute)
BuildRequires:  golang(github.com/google/go-cmdtest)
BuildRequires:  golang(github.com/nats-io/nats-server/v2/server)
BuildRequires:  golang(github.com/nats-io/nats-server/v2/test)
BuildRequires:  golang(golang.org/x/tools/go/packages/packagestest)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%install
%gopkginstall

%if %{with check}
%check
# Up to and including secrets/gcpkms requires network, according to previous maintainer.
%gocheck %{?with_bootstrap:-d secrets/hashivault} \
         %{?with_bootstrap:-d samples/gocdk-secrets} \
         -d docstore/mongodocstore \
         -d internal/cmd/gocdk \
         -d pubsub/gcppubsub \
         -d pubsub/kafkapubsub \
         -d pubsub/rabbitpubsub \
         -d runtimevar/etcdvar \
         -d samples/gocdk-pubsub \
         -d blob/azureblob \
         -d blob/gcsblob \
         -d secrets/gcpkms
%endif

%gopkgfiles

%changelog
%autochangelog
