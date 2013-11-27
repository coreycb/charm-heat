from charmhelpers.contrib.openstack import context

class IdentityServiceContext(context.IdentityServiceContext):
    def __call__(self):
        ctxt = super(IdentityServiceContext, self).__call__()
        if not ctxt:
            return

        # the ec2 api needs to know the location of the keystone ec2
        # tokens endpoint, set in nova.conf
        ec2_tokens = 'http://%s:%s/v2.0/ec2tokens' % (ctxt['service_host'],
                                                      ctxt['service_port'])
        ctxt['keystone_ec2_url'] = ec2_tokens
        return ctxt
