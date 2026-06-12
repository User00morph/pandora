# RAW EXTRACT — System Design Explained: APIs, Databases, Caching, CDNs, Load Balancing & Production Infra

## Source Metadata
- **Title:** System Design Explained: APIs, Databases, Caching, CDNs, Load Balancing & Production Infra
- **Video ID:** adOkTjIIDnk
- **Duration:** 1:49:49
- **Tier:** tier2
- **Playlist:** Pandora Tech Playlist
- **Extracted:** 2026-06-11
- **Domain:** tech-decentralization
- **Word count:** ~21,240

## Transcript (timestamped)

[00:00:00] Most developers cannot design systems or
[00:00:02] features from scratch. They can add to
[00:00:05] someone else's architecture with tasks
[00:00:07] with clear requirements and already on
[00:00:10] mature systems. But, if you ask them to
[00:00:12] design something from the ground up,
[00:00:14] most of them usually will freeze. And
[00:00:17] actually, that is the exact skill that
[00:00:19] separates mid-level developers from
[00:00:21] seniors because seniors are also able to
[00:00:23] make decisions, design trade-offs,
[00:00:26] design the architecture from scratch,
[00:00:29] and make decisions with rough
[00:00:31] requirements. So, companies are not
[00:00:33] paying six figures for people who can
[00:00:35] just code or follow instructions, but
[00:00:38] they are paying for architectural
[00:00:40] decisions, for making the system
[00:00:42] performant, for optimizing the data
[00:00:44] storage, and making the decisions that
[00:00:47] also affect the customers and the
[00:00:50] software that they are building.
[00:00:52] So, in this video, I'm going to teach
[00:00:53] you the exact concepts that I mastered
[00:00:55] to be able to design such systems from
[00:00:58] scratch and also get to senior roles.
[00:01:01] This is how I passed the system design
[00:01:03] interviews without any problems, and
[00:01:05] these are the skills that I learned to
[00:01:07] get to senior level within the second
[00:01:09] year of my career. So, I'm not teaching
[00:01:12] you some theory from books or from
[00:01:14] newsletters. This is what actually works
[00:01:16] in the real jobs and in the real
[00:01:18] interviews.
[00:01:19] So, let's jump into my computer to see
[00:01:21] what we are going to cover in this
[00:01:23] course. First of all, we will start from
[00:01:24] the foundations, the core concepts that
[00:01:27] you need to understand before anything
[00:01:29] else in system design.
[00:01:31] Then, we'll get to API design, which is
[00:01:33] a big part of designing systems, like
[00:01:36] how to actually design APIs that scale
[00:01:38] and also make sense for other developers
[00:01:41] who will be using it.
[00:01:42] Then, we'll get into databases, how to
[00:01:44] choose the right database for different
[00:01:46] scenarios, and design your data layer
[00:01:49] properly.
[00:01:50] Next, we'll get into caching, how to use
[00:01:53] caching, how to use CDNs, load balancing
[00:01:55] to make your systems fast and reliable.
[00:01:58] Then, we'll get into big data processing
[00:02:01] because that's a big topic in itself,
[00:02:03] how to handle large-scale data the right
[00:02:05] way.
[00:02:06] Then, we'll get to designing for
[00:02:08] productions, like how to build systems
[00:02:10] that actually work in the real world,
[00:02:13] not just on your laptop or on a single
[00:02:15] machine.
[00:02:16] And lastly, you can see how I'm
[00:02:17] designing the systems for interviews and
[00:02:20] handling these steps so that you can
[00:02:22] nail these interviews and get the offers
[00:02:25] that you need for getting to senior
[00:02:27] roles. Designing a system to support
[00:02:29] millions of users is challenging, but
[00:02:32] every complex system starts with
[00:02:33] something simple. That's why in this
[00:02:35] lesson, we'll build a basic setup that
[00:02:37] supports just one single user, and then
[00:02:40] we'll gradually expand it as we go.
[00:02:42] Because starting small allows us to
[00:02:44] understand each core component before
[00:02:46] adding more complexity. So, let's start
[00:02:48] with the first step and build a single
[00:02:50] server setup. Imagine that we're setting
[00:02:53] up a system for a small user base. This
[00:02:55] means that everything runs on one single
[00:02:57] server, the web application, the
[00:02:59] database, the cache, and also the other
[00:03:02] components. And this setup allows us to
[00:03:04] visualize the core workings without
[00:03:06] added complexity. Now, let's break down
[00:03:09] how this single server setup handles the
[00:03:11] user requests. We have some users who
[00:03:13] are trying to access our website or our
[00:03:16] API on the server. They can be either
[00:03:18] using the web browser or a mobile app to
[00:03:21] access our server. And on the other
[00:03:23] hand, we have our server, which has the
[00:03:25] necessary files to serve to the web
[00:03:27] browsers and also the necessary API
[00:03:30] endpoints to serve to the mobile app.
[00:03:32] And it is hosted on this example IP
[00:03:34] address. Initially, our users don't have
[00:03:36] this IP address, they have the domain
[00:03:38] which they are trying to access. Let's
[00:03:40] say it's app.demo.com.
[00:03:42] So, if they just type this domain name
[00:03:44] and hit enter, their web browser, for
[00:03:46] example, will contact the DNS, which
[00:03:49] stands for domain name system. This is a
[00:03:51] provider which maps the domains to the
[00:03:54] IP addresses. And in our case, let's say
[00:03:56] our domain name is mapped to the IP
[00:03:58] address, which is the server's IP
[00:04:00] address that we have. So, now this DNS
[00:04:03] provider will send the IP address back
[00:04:05] to the web browser or to the mobile app,
[00:04:08] to our clients. And this IP address is
[00:04:10] our server's IP address. So, now they
[00:04:12] have the location where they are trying
[00:04:14] to send requests. So, with this IP
[00:04:17] address in hand, the user's device sends
[00:04:19] an HTTP request to our server asking for
[00:04:22] specific data. And then, our server
[00:04:24] processes this request and sends back
[00:04:27] the requested data. This might be an
[00:04:29] HTML page for a browser or a JSON
[00:04:31] response for the app, depending on the
[00:04:33] request type. In this setup, traffic
[00:04:36] usually originates from two main
[00:04:38] sources. The first one is the web
[00:04:40] applications, and the second one is the
[00:04:42] mobile applications that are trying to
[00:04:44] access our server. For our web users,
[00:04:47] the server handles the business logic,
[00:04:49] data storage, and also presentation
[00:04:52] using HTML, CSS, and JavaScript. And for
[00:04:55] mobile users, communication typically
[00:04:57] happens over HTTP. These mobile apps
[00:04:59] request data from the server using API
[00:05:02] calls, and JSON is often used for
[00:05:04] responses because it's lightweight and
[00:05:06] easy for mobile devices to interpret.
[00:05:09] Here is an example API request that we
[00:05:11] can receive for our server. It can be a
[00:05:14] get request to our domain/products/the
[00:05:17] ID of that product. And for this
[00:05:19] endpoint, we need to retrieve the
[00:05:20] details of a product. And here is an
[00:05:22] example response that we might send back
[00:05:25] to the client. This is a JSON response,
[00:05:27] which contains the product ID. It
[00:05:29] contains the name of this product, some
[00:05:31] description, the price of the product,
[00:05:34] and some other metadata that is useful
[00:05:36] for the client. And then, this will be
[00:05:38] used by the mobile app or by the web
[00:05:41] browser to display this product on the
[00:05:43] screen. And as we continue, our goal
[00:05:45] will be to identify areas where a single
[00:05:48] server might not be enough for the user
[00:05:50] demand. For now, this setup is ideal for
[00:05:53] small user bases, but it may struggle
[00:05:55] under heavy traffic. So, next we'll
[00:05:57] explore ways to scale each part of the
[00:06:00] system to support more users
[00:06:01] effectively. Some key takeaways that we
[00:06:04] can have from this is that we need to
[00:06:06] start small. We need to begin with a
[00:06:08] straightforward single server setup to
[00:06:10] understand the essential components of
[00:06:12] system architecture. Now, we also
[00:06:15] understand how these requests flow
[00:06:17] through your system, which is
[00:06:18] fundamental for building more scalable
[00:06:20] systems. And we also recognize the
[00:06:23] unique demands for web and mobile
[00:06:25] applications and how they interact with
[00:06:27] your server. And in the next lesson,
[00:06:30] we'll start looking at strategies for
[00:06:32] optimizing and scaling this setup. As
[00:06:34] our user base grows, a single server
[00:06:36] isn't enough to handle the increased
[00:06:38] demand. And to accommodate more users,
[00:06:41] we can separate our web tier, which is
[00:06:43] handling the web and mobile traffic, and
[00:06:45] the data tier, which is managing the
[00:06:47] database. This setup enables us to scale
[00:06:50] each server based on its specific load.
[00:06:53] But, when it comes to choosing the right
[00:06:54] database, how do we know which specific
[00:06:56] database is the best for our specific
[00:06:59] application? When it comes to database
[00:07:01] selection, there are two main options.
[00:07:03] The first option is relational databases
[00:07:06] or RDBMS, which are structured in tables
[00:07:09] and rows. Some popular examples are
[00:07:11] PostgreSQL, MySQL, Oracle database, or
[00:07:14] SQLite. On the other hand, we have
[00:07:16] non-relational or NoSQL databases. These
[00:07:20] are suited for applications that require
[00:07:22] flexibility and fast access to large
[00:07:24] volumes of unstructured data. Some
[00:07:27] examples are Cassandra, MongoDB, Redis,
[00:07:30] or Neo4j. Let's start by exploring the
[00:07:32] relational databases. These databases
[00:07:35] use structured query language or SQL for
[00:07:38] finding and manipulating data. The data
[00:07:41] here is structured in tables, which are
[00:07:43] the fundamental building blocks of SQL
[00:07:45] databases. And these are similar to
[00:07:47] spreadsheets. Each table consists of
[00:07:49] columns, which can be thought as the
[00:07:52] fields or attributes of the table. And
[00:07:54] it also consists of rows, which are
[00:07:56] single records within this table. For
[00:07:58] example, if you imagine a customer's
[00:08:00] table, within this table, we can have
[00:08:02] columns like ID, name, age, and email.
[00:08:05] And for each rows, we can have specific
[00:08:07] customers, like the ID of 123, and the
[00:08:11] name will be John, and the age will be
[00:08:12] 40, and so on. But, what are the
[00:08:15] advantages of using an SQL database?
[00:08:18] First of all, they support complex join
[00:08:20] operations across multiple tables. For
[00:08:22] example, if you imagine we have a
[00:08:24] customer's table and also a product's
[00:08:26] table. And now, we want to create a
[00:08:28] separate table that will connect the
[00:08:30] customers and the products that they
[00:08:32] have ordered. With SQL, you can join
[00:08:35] these two tables together into an orders
[00:08:37] table, and this will hold the
[00:08:39] information about the customer IDs who
[00:08:42] have this order and also the product IDs
[00:08:44] which this customer has ordered. And
[00:08:47] this process of combining two or more
[00:08:49] tables into one table are called join
[00:08:51] operations in SQL. And the other big
[00:08:54] advantage is they provide robust data
[00:08:56] consistency and integrity, especially
[00:08:59] for transactions. Transactions in SQL
[00:09:02] are a sequence of one or more SQL
[00:09:04] operations that are performed as a
[00:09:06] single atomic unit. And each transaction
[00:09:08] in SQL follows the ACID acronym. You can
[00:09:11] think of a transaction example like a
[00:09:13] bank transfer. So, first of all, all of
[00:09:16] the transactions are atomic, which means
[00:09:18] that the entire transaction is treated
[00:09:20] as a single unit, which either
[00:09:21] completely succeeds or completely fails.
[00:09:24] Each transaction is also consistent,
[00:09:26] which means that it transforms the
[00:09:27] database from one valid state to another
[00:09:30] valid state. And they also come with
[00:09:32] isolation, which means that
[00:09:34] modifications made by concurrent
[00:09:36] transactions are isolated from one
[00:09:38] another, and they don't interfere with
[00:09:40] each other. And lastly, they come with
[00:09:42] durability, which means even if the
[00:09:44] system fails or the database server
[00:09:47] fails, the data will still remain there.
[00:09:49] And now, let's have a look at
[00:09:50] non-relational databases. Non-relational
[00:09:53] databases can be in different forms. For
[00:09:56] example, we have document stores like
[00:09:57] MongoDB or you can use wide column
[00:10:00] stores like Cassandra, key-value stores
[00:10:02] like Redis, and graph stores like Neo4j.
[00:10:06] Let's have a look at each of these types
[00:10:07] separately and let's start with the
[00:10:09] document stores. MongoDB is the most
[00:10:12] popular example of a document store and
[00:10:14] the data here is stored in JSON-like
[00:10:16] documents, which allows us to have
[00:10:18] complex data structures within a single
[00:10:20] record. Next, we have wide column stores
[00:10:23] where data is stored in tables, rows,
[00:10:25] and dynamic columns. Some examples here
[00:10:28] are Cassandra or Cosmos DB. The main
[00:10:30] advantage of these databases is they can
[00:10:33] handle massive scales and are very good
[00:10:35] for many write operations. The other
[00:10:37] option is graph databases, which focus
[00:10:40] on storing the entities and their
[00:10:42] relationships as graphs. An example of a
[00:10:44] graph database is Neo4j. For example, in
[00:10:47] Amazon, they use the Neptune graph
[00:10:49] database, which helps them to make you
[00:10:51] product recommendations based on your
[00:10:53] previous orders. And the other popular
[00:10:56] type is key-value stores. Here, data is
[00:10:58] stored in key-value pairs. The biggest
[00:11:01] advantage of key-value stores is their
[00:11:03] simplicity and speed since they are
[00:11:05] primarily stored in RAM. Reading and
[00:11:07] writing to these databases is extremely
[00:11:09] fast compared to other databases. Some
[00:11:12] examples of key-value stores are
[00:11:14] Memcached or Redis. So, that's the main
[00:11:16] four types of NoSQL databases. Now,
[00:11:19] let's have a look at the advantages of
[00:11:21] these NoSQL databases. If you have a
[00:11:23] look at the same example that we had for
[00:11:26] the SQL databases, where we have
[00:11:28] customers and products and we want to
[00:11:30] join them in orders. For example, in
[00:11:32] MongoDB, you could have this as a single
[00:11:34] document, so you could store all of the
[00:11:36] user data, also the orders and products
[00:11:39] in a single document. And because of
[00:11:41] this structure, the NoSQL databases can
[00:11:44] handle highly dynamic and large data
[00:11:46] sets without the structure imposed by
[00:11:48] relational databases. And also, they are
[00:11:51] optimized for low latency and
[00:11:53] scalability. So, when should you use
[00:11:55] relational versus non-relational
[00:11:57] databases? Here is a quick comparison of
[00:12:00] both. If your application data is
[00:12:02] well-structured with clear
[00:12:03] relationships, then you should use SQL
[00:12:05] databases. For example, if you have an
[00:12:08] e-commerce application tracking
[00:12:09] customers and orders, that's a good use
[00:12:12] case of using an SQL database. Next, if
[00:12:15] you need strong consistency and
[00:12:17] transactional integrity. For example, if
[00:12:19] you have a financial application or
[00:12:21] banking system, then you should use the
[00:12:23] SQL databases. However, if your app
[00:12:26] demands super low latency for quick
[00:12:28] responses, then you should go with
[00:12:30] non-relational databases. Or if the data
[00:12:33] is unstructured or semi-structured like
[00:12:35] JSON objects and the relationships
[00:12:37] aren't that crucial, then you should
[00:12:39] also go with NoSQL databases. And
[00:12:42] lastly, if your application requires
[00:12:43] flexible and scalable storage for
[00:12:46] massive data volumes. For example, a
[00:12:48] recommendation engine storing user
[00:12:50] activity data and key-value format, then
[00:12:52] you should also go with NoSQL databases.
[00:12:55] Knowing theory is already a step
[00:12:57] forward, so you already know how to
[00:12:59] design such systems from a high level,
[00:13:02] but this is not enough for getting to
[00:13:04] senior roles and passing the interviews.
[00:13:06] To truly master system design and become
[00:13:09] a confident senior developer who
[00:13:11] commands six-figure salaries, you also
[00:13:14] need hands-on experience building these
[00:13:16] systems from scratch in cloud providers
[00:13:19] like AWS and explaining your
[00:13:21] architectural decisions in real
[00:13:23] interviews. For the next 7 days only,
[00:13:26] you can join the Dev Mastery mentorship
[00:13:28] with a 7-day free trial. You'll get the
[00:13:31] complete system design course,
[00:13:32] real-world projects, and my mentorship
[00:13:35] to become the confident senior engineer
[00:13:38] who doesn't worry about layoffs or AI
[00:13:40] taking your job because you'll have the
[00:13:43] architectural skills that companies
[00:13:44] desperately need and are always willing
[00:13:47] to pay six figures for. Click the link
[00:13:49] in the description to start your free
[00:13:51] trial today.
[00:13:53] Let's explore the two primary approaches
[00:13:55] to scaling, which are vertical and
[00:13:57] horizontal ways of scaling. And we'll
[00:14:00] also see why horizontal scaling is
[00:14:02] generally more suitable for high-traffic
[00:14:04] applications. First, we have the
[00:14:06] vertical scaling or sometimes it's also
[00:14:09] called scale up. This just means that we
[00:14:11] are adding more resources to our
[00:14:13] existing server, meaning RAM, CPU, or
[00:14:16] any other resources that might help us
[00:14:19] to handle more traffic. And this
[00:14:21] approach is simple and works well for
[00:14:23] applications that have low or moderate
[00:14:25] traffic. However, it comes with its
[00:14:28] limitations, which are firstly, resource
[00:14:30] limits. There is a hard cap on how much
[00:14:33] you can add to a single server and
[00:14:35] eventually, you will reach a limit on
[00:14:37] how much you can upgrade your new
[00:14:39] server. And the second reason is lack of
[00:14:42] redundancy, meaning if this server goes
[00:14:45] down, you don't have any other servers
[00:14:47] to serve your users, which means that
[00:14:49] your whole application goes down with
[00:14:51] your single server.
[00:14:53] On the other hand, we have horizontal
[00:14:54] scaling, which is also sometimes called
[00:14:57] scale out. In case of horizontal
[00:14:59] scaling, we are just adding more servers
[00:15:01] to share the load. So, instead of having
[00:15:04] the single server, we might replicate
[00:15:06] and have three of that same server. And
[00:15:08] now, we can share that load between
[00:15:10] these servers instead of handling all of
[00:15:12] them in a single server. Generally, this
[00:15:15] is more suitable for large-scale
[00:15:17] applications as it comes with higher
[00:15:19] fault tolerance and higher fault
[00:15:22] tolerance means if one of our servers
[00:15:24] goes down, we still have two servers
[00:15:26] available, so these two servers can
[00:15:28] continue serving our users while the
[00:15:30] second server recovers from the failure.
[00:15:33] And it also comes with better
[00:15:34] scalability because you can just add
[00:15:37] more servers as needed. Instead of
[00:15:39] having three, you might introduce a
[00:15:41] fourth one, which will handle the new
[00:15:43] incoming traffic. But how do we
[00:15:45] implement the horizontal scaling? In
[00:15:47] case of a single server, we know that
[00:15:49] all of our client requests went to the
[00:15:51] single server, whether it's from mobile
[00:15:53] app or from the desktop. But what if now
[00:15:56] we have three servers to handle all the
[00:15:58] load? How do we distribute the client
[00:16:00] requests? Let's say our mobile app makes
[00:16:03] a request. How do we know where this
[00:16:05] request should go? Whether it should go
[00:16:07] to the server one or server two or to
[00:16:09] server three? And seems like we need to
[00:16:12] have something in the middle, which will
[00:16:14] direct the traffic to the appropriate
[00:16:16] servers. And that part in the middle is
[00:16:19] called a load balancer. We use load
[00:16:21] balancers to distribute the traffic
[00:16:24] across multiple servers. For example,
[00:16:26] here we have three servers, server one,
[00:16:28] two, and three. Whenever we have a new
[00:16:31] request from the clients, the load
[00:16:33] balancer decides where we have the least
[00:16:35] load and then it redirects the traffic
[00:16:37] to that server. And it also controls the
[00:16:40] fault tolerance, meaning if one of our
[00:16:42] server goes down like the server three,
[00:16:45] it will stop sending traffic to the
[00:16:47] first server since it's not available
[00:16:49] anymore and it will send all of the
[00:16:51] traffic to server two and one until the
[00:16:54] server three is available again. And it
[00:16:57] also can make our app more scalable
[00:16:59] because we can introduce a new fourth
[00:17:01] server and any other servers that we
[00:17:03] want and this load balancer will ensure
[00:17:06] that all of the traffic is distributed
[00:17:08] evenly. So, that's the two main
[00:17:10] approaches of scaling, which are
[00:17:12] vertical and horizontal ways of scaling.
[00:17:15] In case of vertical scaling, we are just
[00:17:17] adding more resources to our same
[00:17:19] server, but in case of horizontal
[00:17:21] scaling, we are adding more users to our
[00:17:23] server base and then we use a load
[00:17:25] balancer, which distributes the traffic
[00:17:28] across multiple servers.
[00:17:30] But right now, this load balancer is
[00:17:32] kind of a black box for us because we
[00:17:34] don't understand how does it work, how
[00:17:36] does it take the requests, and how does
[00:17:38] it distribute the traffic. So, let's
[00:17:41] explore that in the next lesson and
[00:17:43] let's see how this exactly works and
[00:17:45] what are the strategies that we use in
[00:17:47] load balancing. Load balancers
[00:17:49] distribute the incoming traffic across
[00:17:51] multiple servers while also ensuring
[00:17:54] that no single server bears too much
[00:17:56] load. But how does it actually happen
[00:17:58] and how does the logic work of
[00:18:00] distributing the incoming traffic?
[00:18:03] To understand load balancers better,
[00:18:05] let's explore seven strategies and
[00:18:07] algorithms that are commonly used in
[00:18:09] load balancing.
[00:18:11] Let's start with round robin, which is
[00:18:12] one of the most popular algorithms.
[00:18:15] That's mainly because it's the simplest
[00:18:17] form of load balancing, where each
[00:18:19] server seen the pool gets a request in
[00:18:22] sequential rotating order, which
[00:18:24] basically means that the first request
[00:18:26] that it receives, it directs it to the
[00:18:28] first server and the next request will
[00:18:31] go to the second server and the third
[00:18:33] one will go to the third server.
[00:18:36] And once the last server is reached, in
[00:18:38] this case, it's the server three, it
[00:18:40] redirects it back to the first server
[00:18:43] and then again to the second server and
[00:18:45] so on.
[00:18:46] This works well for servers with similar
[00:18:48] specifications, meaning if all of our
[00:18:50] three servers have the same capability,
[00:18:53] then round robin will be a good choice
[00:18:55] here.
[00:18:56] Next option is the least connections
[00:18:59] algorithm. It directs traffic to the
[00:19:01] server with the fewest active
[00:19:03] connections. For example, if we have 10
[00:19:05] active connections on the server one, we
[00:19:08] have nine active connections on the
[00:19:10] server two, and we have 40 active
[00:19:12] connections on the server three.
[00:19:15] If it receives a new request from the
[00:19:17] client, it will direct it to the server
[00:19:19] two because it has the least active
[00:19:21] connections at the moment. So, now it
[00:19:23] will have one more connection. And this
[00:19:26] is particularly useful for applications
[00:19:28] where you have sessions of variable
[00:19:30] lengths, meaning that one of your
[00:19:32] sessions might last 10 minutes, the
[00:19:34] other one might last 1 minute and so on.
[00:19:36] And in this case, the load balancer will
[00:19:38] take that into account and it will send
[00:19:41] the traffic to the least connection
[00:19:43] server. The third option is least
[00:19:45] response time.
[00:19:47] This algorithm is more focused on
[00:19:49] responsiveness of the servers.
[00:19:51] Let's say your first server is highly
[00:19:53] responsive, the second one is low
[00:19:55] responsiveness, and the third one is
[00:19:57] medium responsiveness.
[00:19:59] In that case, the load balancer chooses
[00:20:01] the lowest response time and with the
[00:20:03] fewest active connections, meaning first
[00:20:06] it will try to send as many connections
[00:20:08] to the high responsive server as
[00:20:10] possible, but it also takes into account
[00:20:13] the active connections. Let's say this
[00:20:15] server reaches 40 active connections,
[00:20:18] then it will switch to the third server
[00:20:20] because this is the medium
[00:20:21] responsiveness server, and it will send
[00:20:23] some traffic, let's say 20 other
[00:20:25] requests to the medium responsiveness
[00:20:27] server. And after that, it will switch
[00:20:29] to the second server, and it might send
[00:20:31] another 10 requests to this third server
[00:20:34] until it redirects them back to the
[00:20:36] first server.
[00:20:37] This is effective when the goal is to
[00:20:39] provide the fastest response time to
[00:20:41] requests, and you also have different
[00:20:43] servers with different capabilities.
[00:20:46] The fourth option is the IP hash
[00:20:48] algorithm, which determines which server
[00:20:51] receives the request based on the hash
[00:20:53] of the client's IP address. This is
[00:20:55] useful when you want your clients to
[00:20:57] consistently connect to the same server.
[00:21:00] Let's say client one makes a request to
[00:21:02] your load balancer.
[00:21:04] The load balancer will use the client's
[00:21:06] IP address, and based on this, it will
[00:21:08] hash it and send it to appropriate
[00:21:10] server, let's say server two, and all of
[00:21:13] the future requests of the client one
[00:21:15] will go to the load balancer, and it
[00:21:17] will use the same IP hashing algorithm,
[00:21:20] and based on this IP address, it will
[00:21:22] again redirect the user one requests to
[00:21:24] the server two. This is useful if it's
[00:21:27] important for a client to consistently
[00:21:29] connect to the same application.
[00:21:31] If every of your server has some
[00:21:33] information about the clients that are
[00:21:35] connected to it, in that case, the IP
[00:21:38] hashing is a good choice.
[00:21:40] Then there are also weighted algorithms.
[00:21:42] These are variants of the above methods
[00:21:44] that can be also weighted. For example,
[00:21:47] you can have a weighted round robin or
[00:21:49] weighted least connections.
[00:21:51] In this case, servers are assigned two
[00:21:53] weights, typically based on their
[00:21:55] capacity and performance metrics.
[00:21:58] For example, if the first server has 16
[00:22:00] gigs of RAM, the second one has 42, and
[00:22:03] the third one has 64,
[00:22:05] based on the server RAM and other
[00:22:07] metrics, they are assigned two weights,
[00:22:10] and the load balancer takes that into
[00:22:12] account when redirecting the traffic.
[00:22:14] First, it will try to send as many
[00:22:16] connections to the first server as
[00:22:18] possible because it's more weighted,
[00:22:20] meaning it has more performance, and
[00:22:22] then it will try to send the other
[00:22:24] traffic to server two, and then the last
[00:22:27] and small portion will go to server one.
[00:22:30] There are also geographical algorithms,
[00:22:32] which are location-based algorithms that
[00:22:34] direct requests to the server
[00:22:36] geographically closest to the user.
[00:22:39] Let's say this application is for US
[00:22:41] users, so mostly users are connecting to
[00:22:44] this application from US, but we also
[00:22:46] have some part of the users who are
[00:22:48] connecting from Europe. And in our pool
[00:22:51] of servers, we can have one server that
[00:22:53] is located in US East, another server
[00:22:56] that is located in US West, and the last
[00:22:59] server can be located somewhere in
[00:23:01] Europe for the small base of users who
[00:23:03] are located in Europe. So, if a user
[00:23:05] comes from Europe and makes a request to
[00:23:07] this load balancer, it will redirect
[00:23:10] this user to the server in Europe, or if
[00:23:13] a user comes from your US and makes a
[00:23:15] request to this load balancer, it will
[00:23:17] check the location of this US user based
[00:23:19] on its IP address, and then it will
[00:23:21] redirect either to the US East or US
[00:23:24] West. This type of load balancing is
[00:23:26] useful for global services, where
[00:23:29] latency reduction is important.
[00:23:31] And the last most popular type is
[00:23:33] consistent hashing. In this case, we use
[00:23:36] a hash function to distribute data
[00:23:38] across various nodes. We have a hash
[00:23:40] function inside of a load balancer, and
[00:23:43] we usually imagine a hash space along
[00:23:45] with this that forms a hash ring, like a
[00:23:48] circle. This hash function forms a
[00:23:50] circle, where we have the servers, for
[00:23:52] example, the server one, two, and three,
[00:23:55] which are located in front of this load
[00:23:57] balancer.
[00:23:58] So, whenever a new request comes from a
[00:24:01] user, this hash function takes the IP
[00:24:03] address of that user, and then based on
[00:24:05] that, it locates this user on this hash
[00:24:08] ring. Let's say it locates it somewhere
[00:24:10] here, and then depending to which server
[00:24:12] this point is closest to, for example,
[00:24:15] in this case, this is closer to server
[00:24:17] two, it redirects the traffic to that
[00:24:19] server.
[00:24:20] This is a bit more complicated way of
[00:24:23] load balancing, but it also ensures that
[00:24:25] the same client consistently connects to
[00:24:27] the same server, like in case of IP
[00:24:30] hashing.
[00:24:31] We also talked about that whenever a
[00:24:33] server goes down, this load balancer
[00:24:35] ensures that traffic is not redirected
[00:24:37] to that server.
[00:24:39] But how does it know in the first place
[00:24:40] that this server is not available?
[00:24:43] For that, most load balancers come with
[00:24:45] health check features, which means that
[00:24:47] they are consistently monitoring the
[00:24:49] servers by sending a health check
[00:24:51] request to all of these servers, and
[00:24:54] they have the information about which
[00:24:56] servers are online, let's say the first
[00:24:58] three servers are available, and which
[00:25:00] ones are offline, which means the fourth
[00:25:02] server, which is offline.
[00:25:04] So, whenever it detects a failure in the
[00:25:06] health check, it knows that this fourth
[00:25:08] server is not available anymore, and
[00:25:11] based on that information, if the next
[00:25:13] request comes from the client, it won't
[00:25:16] redirect them to the fourth server until
[00:25:18] the health check again succeeds, and it
[00:25:20] knows that the fourth server is back
[00:25:22] online.
[00:25:24] And now let's see some load balancer
[00:25:25] examples and what are these actually,
[00:25:28] how do we implement them? First, we have
[00:25:30] software load balancers. For example,
[00:25:32] Nginx is probably the most common type
[00:25:35] of the software load balancer.
[00:25:37] It has other features, and it's also
[00:25:39] used as a web server, but it also offers
[00:25:42] the functionality of a load balancer.
[00:25:45] Typically, you install this Nginx on
[00:25:47] your server and then configure the
[00:25:49] servers that should be load balanced and
[00:25:51] also the algorithm. And as you can see,
[00:25:53] it also comes with health checks, which
[00:25:55] I mentioned. So, you can set up health
[00:25:57] checks among your servers, and then this
[00:26:00] will consistently monitor your servers,
[00:26:02] and whenever one of your server goes
[00:26:04] down, it won't redirect traffic to that
[00:26:06] server.
[00:26:07] Another example of a software load
[00:26:09] balancer is HAProxy, which is an
[00:26:12] open-source software that again you can
[00:26:14] install on your server and configure as
[00:26:16] you want. But apart from software load
[00:26:19] balancers, we also have hardware load
[00:26:21] balancers. For example, we have the F5
[00:26:24] load balancer, which is a widely used
[00:26:26] hardware load balancer known for its
[00:26:28] high performance and feature set.
[00:26:31] Next, we have Citrix, which also comes
[00:26:33] with load balancing functionality, and
[00:26:35] again, this is a hardware type of load
[00:26:37] balancer.
[00:26:39] But if you don't want to configure all
[00:26:40] of that yourself on your server or as a
[00:26:43] hardware, then the easier solutions are
[00:26:45] cloud-based load balancers. For example,
[00:26:48] AWS comes with Elastic Load Balancing,
[00:26:50] and if you have your servers also set up
[00:26:53] in AWS, then it's pretty easy to
[00:26:55] configure this with your servers. And
[00:26:57] you can also see it in the benefits that
[00:26:59] it automatically comes with security,
[00:27:02] automatic scaling, meaning that it will
[00:27:04] automatically add new servers to the
[00:27:06] pool if the demand increases of your
[00:27:08] application, and it also comes with
[00:27:10] monitoring, which is the same as health
[00:27:12] checks, so you don't have to set it up
[00:27:14] yourself. And other examples similar to
[00:27:17] AWS are Azure's load balancer and Google
[00:27:20] Cloud's load balancing. Now, let's talk
[00:27:23] about the concept which is called a
[00:27:25] single point of failure in system
[00:27:27] design. This is one part of your whole
[00:27:29] system that whenever it fails, it will
[00:27:32] bring the entire system down with it.
[00:27:34] So, to put it simply, it is any
[00:27:36] component that could cause the whole
[00:27:39] system to fail whenever it stops
[00:27:41] working.
[00:27:42] For example, if you imagine this setup
[00:27:44] when the clients connect to our load
[00:27:47] balancer, and then load balancer
[00:27:49] distributes them to the APIs, and then
[00:27:51] we have a single database, which is used
[00:27:54] for all APIs servers. Database here is
[00:27:57] one example of a single
[00:28:01] point of failure. Whenever this database
[00:28:04] goes down, all of these APIs won't be
[00:28:06] able to connect to the database, and
[00:28:09] because of that, all of these also won't
[00:28:11] function properly, and our clients won't
[00:28:13] be able to receive So, having single
[00:28:15] points of failures in your system is
[00:28:18] problematic because they can create
[00:28:20] vulnerabilities.
[00:28:21] The first obvious downside is the
[00:28:23] reliability because a single failure,
[00:28:26] like the failure of this database, can
[00:28:28] take the entire system down, which could
[00:28:30] mean business losses because users are
[00:28:32] not able to access our platform. Maybe
[00:28:35] they are also not able to access the
[00:28:37] checkout page or any other parts of the
[00:28:40] system, which can bring losses in the
[00:28:42] business.
[00:28:43] It is also an issue for scalability
[00:28:46] because systems that have single point
[00:28:48] of failures like this can often struggle
[00:28:51] to scale as each component will add a
[00:28:53] risk of failing this single part.
[00:28:56] And the last part, it also brings a
[00:28:58] security issue because if you have a
[00:29:00] single point of failure in your system,
[00:29:02] like the load balancer, attackers can
[00:29:04] compromise this point by sending huge
[00:29:07] traffic to it, and if this fails, the
[00:29:09] whole system will go down.
[00:29:11] We will talk about how to avoid the
[00:29:13] database single points of failure in the
[00:29:15] databases section, but in this section,
[00:29:18] we can have a look at how to avoid the
[00:29:20] load balancers to become a single point
[00:29:23] of failure because right now, we have
[00:29:25] only one load balancer setup. And if
[00:29:28] this load balancer goes down, then all
[00:29:30] of our users won't be able to access
[00:29:32] this point, and they will also not be
[00:29:34] able to access to our APIs.
[00:29:37] The first strategy is adding redundancy
[00:29:39] to our system. This means that we can
[00:29:42] use more than one load balancer, and for
[00:29:44] example, if the second load balancer
[00:29:46] goes down, users won't be able to
[00:29:48] connect to this load balancer, but in
[00:29:51] that case, we can redirect all of the
[00:29:53] traffic to the first one, and then this
[00:29:55] first load balancer will balance the
[00:29:57] load between those servers. And we will
[00:30:00] monitor the health of the second load
[00:30:02] balancer, and whenever it's back online
[00:30:04] and it's again available, we will also
[00:30:07] redirect 50% of the traffic to the
[00:30:09] second load balancer.
[00:30:11] Another strategy is to use health checks
[00:30:14] and monitoring
[00:30:16] themselves. As we saw, load balancer can
[00:30:19] do health checks for the servers and
[00:30:21] check whenever our servers are online or
[00:30:23] offline. We can do the same strategy for
[00:30:26] load balancers, and we can check their
[00:30:28] health continuously, and whenever one of
[00:30:31] our load balancer goes down, we will
[00:30:33] know that we shouldn't redirect any
[00:30:35] traffic to this load balancer until it
[00:30:37] is back online. And the third common
[00:30:40] type is self-healing systems, which
[00:30:42] means that we again monitor the health
[00:30:45] of our load balancer, and if at any
[00:30:47] point we detect that it goes down, we
[00:30:49] will replace this with a new load
[00:30:51] balancer, which is basically an instance
[00:30:54] of the same load balancer, and this way
[00:30:56] we won't cause any interruptions, and
[00:30:58] our clients will be able to connect to
[00:31:00] this new load balancer. Welcome to this
[00:31:03] section, where you will learn the
[00:31:05] fundamental principles of API design,
[00:31:07] which will enable you to create
[00:31:09] efficient, scalable, and also
[00:31:11] maintainable interfaces between software
[00:31:14] systems. Here is what we're going to
[00:31:16] cover in this lesson. We'll start from
[00:31:19] what APIs are and what is their role in
[00:31:21] system architecture. Then we'll cover
[00:31:24] the three most commonly used API styles,
[00:31:26] which are REST, GraphQL, and gRPC. We'll
[00:31:30] discuss the four essential design
[00:31:32] principles that make great APIs, and
[00:31:35] also how application protocols influence
[00:31:38] the API design decisions. We'll also
[00:31:40] cover the API design process, so
[00:31:43] starting from the design phase to
[00:31:45] development phase to deployment. So
[00:31:47] we'll see how that process looks like.
[00:31:49] So let's start by understanding what is
[00:31:51] an API. API stands for application
[00:31:54] programming interface, which defines how
[00:31:56] software components should interact with
[00:31:58] each other.
[00:31:59] Let's say on one side you have the
[00:32:01] client, which is either the mobile phone
[00:32:03] or the browser of this user, and on the
[00:32:06] other side you have the server, which
[00:32:07] will be responding to the requests.
[00:32:10] So API here is just a contract that
[00:32:13] defines these terms, which are all
[00:32:15] requests can be made. So it provides us
[00:32:17] with an interface on how to make these
[00:32:19] requests, meaning what endpoints do we
[00:32:22] have, what methods can we use, and so
[00:32:24] on. Also, what responses can we expect
[00:32:27] from this server for a specific
[00:32:29] endpoint.
[00:32:30] So first of all, it is an abstraction
[00:32:32] mechanism because it hides the
[00:32:34] implementation details while exposing
[00:32:37] the functionality. For example, we can
[00:32:39] make a request to save a user data in
[00:32:42] this server, but we don't care at all
[00:32:44] about how the logic applies behind the
[00:32:47] scenes inside of this server. So we only
[00:32:49] care about the interface that is
[00:32:51] provided through this API, and we only
[00:32:54] use that endpoint, and we store the user
[00:32:56] without even knowing about the
[00:32:58] implementation details. And it also sets
[00:33:01] the service boundaries because it
[00:33:03] defines clear interfaces between systems
[00:33:06] and components. So this allows us to
[00:33:08] have multiple servers. We can have one
[00:33:11] server that is responsible for managing
[00:33:13] the users. We can have another one that
[00:33:15] is responsible for some other records,
[00:33:17] let's say for managing the posts, and so
[00:33:19] on.
[00:33:20] So this allows different systems to
[00:33:23] communicate regardless of their
[00:33:25] underlying implementation, like client
[00:33:27] browsers with servers or servers with
[00:33:30] another servers, and so on.
[00:33:32] Now let's focus on the most important
[00:33:34] API styles you will encounter during the
[00:33:37] design phase. These are RESTful,
[00:33:39] GraphQL, and gRPC. The most common one
[00:33:42] out of these is REST, which stands for
[00:33:45] representational state transfer. These
[00:33:47] type of APIs use resource-based approach
[00:33:50] by using the HTTP methods as a protocol.
[00:33:54] One of the advantages of REST APIs is
[00:33:56] that they are stateless, meaning that
[00:33:58] each request contains all of the
[00:34:00] information needed to process it, and we
[00:34:02] don't need any prior requests to be able
[00:34:05] to process the current request. And it
[00:34:07] uses the standard methods on HTTP
[00:34:10] protocol, which are GET for fetching
[00:34:12] data, POST for storing data, PUT or
[00:34:15] PATCH for updating data, and DELETE for
[00:34:18] deleting data.
[00:34:19] So based on its characteristics, the
[00:34:22] REST is most commonly used in web and
[00:34:24] mobile applications. Next, we have
[00:34:27] GraphQL, which is the second most common
[00:34:29] API style after the REST APIs. GraphQL
[00:34:33] is a query language that allows clients
[00:34:35] to request exactly what they need. This
[00:34:38] means that it comes with a single
[00:34:40] endpoint for all of the operations, and
[00:34:42] we can choose what we are expecting to
[00:34:45] receive from this API by providing the
[00:34:47] payload in the request.
[00:34:49] And the operations here are called query
[00:34:52] whenever we are retrieving data or
[00:34:54] mutation whenever we are updating data.
[00:34:56] So this is the equivalent in PUT or
[00:34:59] PATCH or POST in the RESTful APIs. And
[00:35:03] there is also a subscription in
[00:35:05] operations, which is for real-time
[00:35:06] communication. The advantage of GraphQL
[00:35:09] APIs is that it allows us to have
[00:35:11] minimal round trips. Let's say we need
[00:35:13] some data that in RESTful APIs, we will
[00:35:16] need to make three requests to get all
[00:35:18] of this data. In GraphQL case, we can
[00:35:21] make a single request and get all of
[00:35:23] this data, avoiding the unnecessary two
[00:35:26] requests that we will otherwise have to
[00:35:28] make in RESTful.
[00:35:30] And because of that, this is the
[00:35:31] recommended option for complex UIs. So
[00:35:34] wherever you have some complex UIs where
[00:35:36] on one page you might need different
[00:35:38] data, on another page you might need
[00:35:40] some other complex nested data. In these
[00:35:42] cases, GraphQL is the better choice over
[00:35:45] RESTful APIs.
[00:35:47] And the last option is gRPC. I would say
[00:35:49] this is the least common one out of
[00:35:51] these three.
[00:35:52] gRPC is a high-performance RPC
[00:35:55] framework, which is using protocol
[00:35:57] buffers for communication.
[00:36:00] The methods in gRPC are defined as RPCs
[00:36:04] in the proto files, and it supports
[00:36:06] streaming and bidirectional
[00:36:08] communication. This is an excellent
[00:36:10] approach for microservices especially,
[00:36:13] and internal system communication, as it
[00:36:16] is more efficient when you're working
[00:36:17] between servers compared to GraphQL or
[00:36:20] compared to RESTful APIs.
[00:36:23] So the difference between REST, GraphQL,
[00:36:25] and gRPC APIs is kind of clear, but
[00:36:28] let's also clarify the real difference
[00:36:30] between REST and GraphQL APIs on
[00:36:32] examples.
[00:36:34] So as you saw, REST comes with
[00:36:35] resource-based endpoints. For example,
[00:36:38] here if we take a look at these
[00:36:39] requests, you can see that the resource
[00:36:41] here is users. So you always expect to
[00:36:44] see some users endpoint or some
[00:36:46] followers endpoint or let's say posts
[00:36:49] endpoint. So it is resource-based. And
[00:36:52] sometimes we might need to make multiple
[00:36:54] requests for getting the related data.
[00:36:56] As you can see here, we need let's say
[00:36:58] the user details, but we also need the
[00:37:01] user posts and followers. So in this
[00:37:03] case, we need to make three requests to
[00:37:05] get all of this data.
[00:37:07] And it uses HTTP methods to define
[00:37:10] operations. As you can see, these are
[00:37:11] HTTP endpoints, and we are using the GET
[00:37:14] method specifically. And the response
[00:37:17] structures are fixed, meaning if you got
[00:37:19] one response for this specific user,
[00:37:22] next time you can expect to have exactly
[00:37:24] the same response structure. Maybe some
[00:37:26] data will be modified, but the structure
[00:37:29] always remains the same. And it also
[00:37:31] provides explicit versioning. So as you
[00:37:33] can see, it comes with V1 for the V1
[00:37:35] API, then later if it got a major
[00:37:38] upgrade, then this will become V2, and
[00:37:40] so on. And you can use the headers on
[00:37:43] the requests to leverage the HTTP
[00:37:45] caching on RESTful APIs. Now if we
[00:37:48] compare that to GraphQL APIs, it comes
[00:37:51] with a single endpoint for all
[00:37:53] operations. So mostly it is {slash}
[00:37:56] GraphQL or {slash} some API endpoint
[00:37:58] that is commonly used for all
[00:38:00] operations. And in this case, we will
[00:38:03] use a single request to get the precise
[00:38:05] data that we need, and we will use the
[00:38:07] query language of GraphQL.
[00:38:10] This is what the query language looks
[00:38:12] like. As you can see, we start with a
[00:38:14] query, and then we define what we need.
[00:38:16] For example, we need the user with ID
[00:38:18] 123. Then we need the name of the user,
[00:38:21] the posts, and then we define whatever
[00:38:24] we need from the posts. Maybe we need
[00:38:26] only title and content, and nothing
[00:38:28] more. And also the followers, and what
[00:38:31] we need from followers, maybe only
[00:38:32] names. So this allows us to be more
[00:38:35] efficient in our requests compared to
[00:38:37] RESTful APIs, where we will need to make
[00:38:40] three requests for this same data.
[00:38:43] This means that client needs to specify
[00:38:45] the response structure, and in this
[00:38:47] case, the schema evolution is without
[00:38:50] versioning. So here as you saw, it is
[00:38:52] with V1, V2, and so on. In this case,
[00:38:55] the schema usually evolves without
[00:38:57] versioning, but there is also a common
[00:38:59] pattern to start versioning the fields.
[00:39:02] For example, you can have followers V2,
[00:39:05] and that will be the second type of
[00:39:07] followers schema. But you can also go
[00:39:10] without versioning, so you can just
[00:39:12] start modifying the followers or posts
[00:39:15] if you are sure that there are no other
[00:39:17] clients using your old API.
[00:39:20] And in this case, you can leverage the
[00:39:22] application level caching instead of the
[00:39:24] HTTP caching.
[00:39:26] Now let's discuss the major design
[00:39:28] principles that will allow us to create
[00:39:31] consistent, simple, secure, and also
[00:39:33] performant APIs.
[00:39:35] Ultimately, the best API is the one that
[00:39:38] we can use without even reading the
[00:39:40] documentation. For example, if you saw
[00:39:42] the previous endpoints in the users, you
[00:39:45] see that we have {slash} users {slash} 1
[00:39:48] 2 3, and obviously we are expecting to
[00:39:50] get the user details of this specific
[00:39:53] user. And if you make a request, for
[00:39:55] example, to that endpoint to fetch user
[00:39:57] details, but then you find out that it
[00:39:59] also update some followers or something
[00:40:02] while making this request, then
[00:40:04] obviously that is a very bad type of API
[00:40:06] as we didn't expect it to do such
[00:40:08] operations.
[00:40:10] So, first of all, the good API should be
[00:40:12] consistent, meaning it should use the
[00:40:14] consistent naming, casing, and patterns.
[00:40:18] For example, if you use camel case in
[00:40:20] one of the endpoints, let's say you have
[00:40:22] user details, and you do this in camel
[00:40:25] case, but in another case you do it with
[00:40:27] a snake case, like user {slash} details,
[00:40:31] then this is not common, and this is not
[00:40:33] consistent.
[00:40:35] The second key principle is to keep it
[00:40:37] very simple and focus on core use cases
[00:40:40] and intuitive design.
[00:40:42] So, you should minimize complexity and
[00:40:45] aim for designs that developers can
[00:40:47] understand quickly without even maybe
[00:40:49] reading the documentation. And
[00:40:51] simplicity again comes down to this,
[00:40:53] which is the best API is one that
[00:40:55] developers can use without even reading
[00:40:58] the documentation.
[00:41:00] Next, obviously it has to be secure, so
[00:41:02] you have to have some sort of
[00:41:03] authentication and authorization between
[00:41:06] users. Also, if you have inputs, then
[00:41:08] you need to make sure that these are
[00:41:10] validated, and you should also apply
[00:41:12] rate limiting. So, these are the most
[00:41:14] basic things that you have to do to keep
[00:41:17] your APIs secure.
[00:41:19] And the last pillar is performance, so
[00:41:21] you should design for efficiency with
[00:41:24] appropriate caching strategies with
[00:41:26] pagination. If you have a large amount
[00:41:29] of data, let's say thousands of posts,
[00:41:31] you don't want to retrieve all of these
[00:41:33] whenever they make a request to get the
[00:41:35] post, so you should always have
[00:41:37] pagination with some limit and offset.
[00:41:40] Also, the payloads, meaning the data
[00:41:42] that you will send back, should be
[00:41:44] minimized. And also, whenever possible,
[00:41:46] you should reduce the round trips. So,
[00:41:49] if you have the opportunity to send some
[00:41:51] small data along with the request of one
[00:41:54] of the endpoints, then it's better to do
[00:41:56] this if you know that you're going to
[00:41:58] use it instead of making another
[00:42:00] endpoint for making a request to get the
[00:42:02] same data.
[00:42:04] Now, each of these APIs use different
[00:42:06] protocols, and we will learn more about
[00:42:09] these in the next lesson, but basically
[00:42:11] your protocol choice will fundamentally
[00:42:13] shape your API design options.
[00:42:16] For example, the features of HTTP
[00:42:18] protocol directly enable restful
[00:42:21] capabilities, so it makes more sense to
[00:42:23] use HTTP along with restful APIs because
[00:42:27] it also provides you with status codes,
[00:42:29] and these are great to be used with
[00:42:31] crowd operations that you will have in
[00:42:33] restful APIs. On the other hand, web
[00:42:36] sockets, which is another type of
[00:42:38] protocol, enable real-time data and also
[00:42:41] enable bidirectional APIs. So, these can
[00:42:44] be used along with real-time APIs
[00:42:46] wherever you need some chat application
[00:42:49] or some video streaming. This is a good
[00:42:51] use case of web socket APIs.
[00:42:54] In case of GraphQL APIs, you again will
[00:42:56] use the HTTP protocol instead of web
[00:42:59] sockets or gRPC.
[00:43:01] gRPC, on the other hand, can be used
[00:43:03] among with microservices in your
[00:43:06] architecture to make it faster compared
[00:43:08] to HTTP. So, your protocol choice will
[00:43:12] affect the API structure and also the
[00:43:14] performance and capabilities.
[00:43:17] Therefore, you should choose it based on
[00:43:18] its limitations and strengths, and the
[00:43:21] one that makes more sense in the type of
[00:43:24] API that you'll be developing.
[00:43:26] Now, let's discuss the API design
[00:43:28] process. It all starts with
[00:43:30] understanding the requirements, which is
[00:43:32] identifying core use cases and user
[00:43:35] stories that you will need to develop.
[00:43:37] Also, defining the scope and boundaries
[00:43:40] because if it's a huge API, then you
[00:43:43] probably won't develop all of the
[00:43:45] features at once, so you should scope it
[00:43:47] to some specific features that you'll be
[00:43:49] developing, and also what are out of
[00:43:52] scope for now.
[00:43:53] Then you should determine the
[00:43:55] performance requirements, and
[00:43:56] specifically in your API case, what will
[00:43:59] be the bottlenecks and where you need to
[00:44:01] make sure that it's performant.
[00:44:03] And you should also not overlook the
[00:44:05] security constraints, so you should
[00:44:07] implement all of the basic features like
[00:44:10] authentication, authorization, the rate
[00:44:12] limiting, but maybe some more stuff
[00:44:15] depending on the API that you'll
[00:44:16] develop. When it comes to design
[00:44:18] approaches, there are couple of ways to
[00:44:21] go about it. The first one is top-down
[00:44:23] approach, which is you start with
[00:44:25] high-level requirements and workflows.
[00:44:28] This is more common in interviews where
[00:44:30] they give you the requirements on what
[00:44:32] the API will be about, and then you
[00:44:35] start defining what the endpoints will
[00:44:37] be, what the operations will be, and so
[00:44:40] on. But there is also the bottom-up
[00:44:42] approach, which is if you have existing
[00:44:44] data models and capabilities, then you
[00:44:47] should design the API based on this. So,
[00:44:49] this is more common when you're working
[00:44:51] in a company, and they already have
[00:44:54] their data models and capabilities of
[00:44:56] their APIs. So, you should take that
[00:44:58] into account when designing the API.
[00:45:01] And we also have contract-first
[00:45:03] approach, which is you define the API
[00:45:05] contract before implementation, meaning
[00:45:08] what the requests should look like and
[00:45:10] what the responses should look like. And
[00:45:13] this is more similar to top-down
[00:45:15] approach, and this is also commonly used
[00:45:17] in interviews.
[00:45:18] When it comes to life cycle management
[00:45:20] of APIs, it starts with the design phase
[00:45:23] where you design the API, discuss the
[00:45:26] requirements and the expected outcomes
[00:45:29] of the API. And only after that you can
[00:45:32] start the development and maybe local
[00:45:34] testing of your API.
[00:45:36] After that, you usually deploy and
[00:45:39] monitor it, so you do some more testing,
[00:45:41] but now on staging or on production. But
[00:45:44] then it also comes the maintenance
[00:45:46] phase, and this is why it's important to
[00:45:48] develop it with keeping the simplicity
[00:45:51] in place, so it will be easier for you
[00:45:53] to maintain or for other developers to
[00:45:56] maintain in the future.
[00:45:58] And lastly, APIs also go through
[00:46:00] deprecation and retirement phase. So,
[00:46:02] some APIs eventually get deprecated
[00:46:05] because there might come up with a new
[00:46:07] version of the API that you should use,
[00:46:09] or let's say you are transitioning from
[00:46:12] V1 to V2 API. So, that's also the
[00:46:15] deprecation phase of the V1 API.
[00:46:18] So, developing APIs is not only in the
[00:46:21] development phase, as you might assume.
[00:46:23] It's not just coding, so the big part of
[00:46:25] it is designing it and also keeping it
[00:46:28] maintainable, and also eventually you
[00:46:31] might need to retire it at the end.
[00:46:33] So, let's recap and see what our next
[00:46:35] steps are. We learned what APIs are and
[00:46:38] about the most dominant three type of
[00:46:41] API styles, which are RESTful, GraphQL,
[00:46:44] and gRPC.
[00:46:46] We've covered the four key principles
[00:46:48] that will guide us when creating API
[00:46:50] designs effectively. And you now also
[00:46:53] understand how the design choice of your
[00:46:56] protocol will influence the design of
[00:46:58] your API and also the whole API design
[00:47:01] process from start to finish.
[00:47:03] But we didn't discuss the limitations
[00:47:06] and strengths of these API protocols, so
[00:47:09] that's why in the next lesson, we will
[00:47:11] learn all about the API protocols that
[00:47:13] we can use with API design, and which
[00:47:16] one we should choose based on the
[00:47:18] requirements of our API. Choosing the
[00:47:20] wrong protocol for our API can lead to
[00:47:23] performance bottlenecks and also
[00:47:25] limitations in functionality. That's why
[00:47:27] we need to first understand these
[00:47:29] protocols, which will allow us to build
[00:47:31] APIs that meet our specific user
[00:47:33] requirements for latency, throughput,
[00:47:36] and also interaction patterns. That's
[00:47:39] why in this lesson, we'll cover the role
[00:47:41] of API protocols in the network stack,
[00:47:44] the two fundamental protocols, which are
[00:47:46] HTTP and HTTPS, and also their
[00:47:49] relationship to APIs.
[00:47:51] Also, another common type of protocol,
[00:47:53] which is web socket for real-time
[00:47:55] communication. We'll also cover advanced
[00:47:58] message queuing protocol, which is
[00:48:00] commonly used for asynchronous
[00:48:01] communication. And lastly, we'll cover
[00:48:04] the gRPC, which is Google's remote
[00:48:06] procedure call, and it is also another
[00:48:09] common type of protocol used commonly
[00:48:11] within servers. Let's start by
[00:48:13] understanding the application protocols
[00:48:15] in network stack. Application layer
[00:48:18] protocols sit at the top of network
[00:48:20] stack, building on top of protocols like
[00:48:23] TCP and UDP, which are at the transport
[00:48:26] layer. These protocols at application
[00:48:29] layer define the message formats and
[00:48:32] structures, also the request-response
[00:48:34] patterns, and management of the
[00:48:36] connections and error handling.
[00:48:39] Now, below that we have many other
[00:48:41] layers like the network layer or data
[00:48:43] link layer or even physical layers, but
[00:48:46] when building APIs, we are mostly
[00:48:48] concerned with the API layer protocols,
[00:48:51] which are HTTP, HTTPS, web sockets, and
[00:48:54] so on. The most common type of protocol,
[00:48:57] and also the foundation of web APIs, is
[00:49:00] HTTP, which stands for Hypertext
[00:49:02] Transfer Protocol. This is the typical
[00:49:05] interaction between client and server
[00:49:07] when they are interacting over HTTP. As
[00:49:09] you can see, client always sends a
[00:49:11] request, and they define the method,
[00:49:13] which can be get, post, or other
[00:49:15] methods, and they define the resource
[00:49:17] URL, which can be at {slash} API {slash}
[00:49:20] products. Let's say they are requesting
[00:49:22] data for this specific ID of the
[00:49:24] product, and they also define the
[00:49:26] version of the HTTP protocol that they
[00:49:29] are using.
[00:49:30] They also define the host, which is the
[00:49:32] domain of your server where the
[00:49:34] information is accessed, and usually
[00:49:37] they also authenticate before accessing
[00:49:39] any resources. So, it can be either a
[00:49:41] bearer token or a basic authentication,
[00:49:44] OAuth, and so on. So, once the request
[00:49:47] is authenticated in the server, it
[00:49:49] receives the response, which is in
[00:49:51] similar format, and it's in HTTP
[00:49:53] response. So, you get the HTTP version,
[00:49:56] which is again the same as you requested
[00:49:58] with, and the status code, which can be
[00:50:01] 200 if it was successful, or it can be
[00:50:03] 400 if the client was error, or 500 if
[00:50:07] the error happened in server, and so on.
[00:50:09] You receive the content type, which can
[00:50:11] be usually application JSON, but it can
[00:50:14] also be a static web page or something
[00:50:16] else. And there are many other headers
[00:50:19] that you can control, like controlling
[00:50:21] cache, you can use the cache control
[00:50:23] header or some other properties, but
[00:50:25] these are the main things that you would
[00:50:27] notice in HTTP request-response cycles.
[00:50:30] Now, when it comes to methods, you have
[00:50:32] get for retrieving data, post for
[00:50:35] creating data in the server, put or
[00:50:37] patch for updating data partially or
[00:50:40] fully, and delete for removing data from
[00:50:43] the server. And when it comes to status
[00:50:46] codes, which are received by the server,
[00:50:48] so you have 200 series, which are
[00:50:50] successful cases. You have 300 for
[00:50:52] redirection. 400 means that client made
[00:50:55] an error in the request, so this is an
[00:50:57] issue from client side, or 500, which
[00:51:00] means that server made an error, or like
[00:51:02] some error happened in the server, which
[00:51:04] that this is the issue in the server.
[00:51:07] And these are the common headers, like
[00:51:09] content type, which is defined by the
[00:51:11] server usually, but also from the
[00:51:13] client. Authorization for making a
[00:51:15] request and authorizing to the server,
[00:51:18] accept headers, cache control, user
[00:51:20] agent, and there are more headers, but
[00:51:22] these are the common ones. Then we also
[00:51:25] have HTTPS, which is basically the same
[00:51:27] HTTP protocol, but with some sort of TLS
[00:51:30] or SSL encryption, which means that our
[00:51:33] data is now protected in transit when we
[00:51:36] are making requests. So, it adds a
[00:51:38] security layer through these TLS or SSL
[00:51:41] certificates and encryption, and it
[00:51:43] protects data in the transit. And
[00:51:46] benefits of HTTPS is obviously your data
[00:51:48] is encrypted in the transit. It comes
[00:51:51] with data integrity, and you also
[00:51:53] authenticate users before providing any
[00:51:55] data, and it also adds SEO benefits. And
[00:51:58] you have many risks when you are using
[00:52:00] HTTP only without any encryption. So,
[00:52:03] the golden standard is to always use
[00:52:05] HTTPS in servers.
[00:52:07] The next type of protocols are
[00:52:09] WebSockets. While we have HTTP, which is
[00:52:12] very good at request-response patterns,
[00:52:14] sometimes HTTP has limitations. For
[00:52:17] example, let's say you're polling some
[00:52:19] data. Let's say this is a user chat, so
[00:52:21] you have the client and server. On the
[00:52:23] client side, you have the user chat, and
[00:52:25] on the server, you have the messages
[00:52:27] between two users.
[00:52:29] When one of the users messages the
[00:52:31] other, it sends a request to the server
[00:52:34] to notify that a message has been sent,
[00:52:36] and it receives a response from the
[00:52:38] server, maybe the messages from the
[00:52:40] other users if there are any. And then
[00:52:43] next time, if you need to know if you
[00:52:45] have new messages, you need to make
[00:52:47] again another request to the server, and
[00:52:50] maybe you don't have any new messages,
[00:52:52] so you will receive an empty response
[00:52:54] with no new data. So, this was basically
[00:52:56] a unnecessary request-response cycle,
[00:52:59] and you might request from some other
[00:53:01] time, let's say from 1 minute, and
[00:53:03] receive a response. Now you have some
[00:53:05] messages, but it can be also empty
[00:53:07] again. So, this way is not ideal for
[00:53:10] real-time communication. As you can see,
[00:53:12] you get increased latency, you waste
[00:53:15] some bandwidth with making requests that
[00:53:17] are empty, and you also use the server
[00:53:19] resources without the need of making
[00:53:22] requests to the server. And for such
[00:53:24] cases, we have WebSockets, which solve
[00:53:27] this issue. So, in WebSocket, you have
[00:53:29] usually a handshake that is happening
[00:53:31] within the first request, and now you
[00:53:34] have both like two-way communication
[00:53:36] between client and the server, which
[00:53:38] means that once the handshake is been
[00:53:40] made, the server can independently
[00:53:43] decide to push data to the client. Let's
[00:53:45] say now you have two new messages on the
[00:53:48] server. So, server can decide to send
[00:53:50] these messages to the client without
[00:53:52] even client requesting for it. But
[00:53:55] client can still request data, so if
[00:53:57] client needs some external data or more
[00:54:00] data from the server, it can still make
[00:54:02] requests, but server is now also able to
[00:54:05] independently push data to the client.
[00:54:08] So, this is what unlocks the real-time
[00:54:10] data with minimal latency. As soon as
[00:54:12] you have some new data in the server, it
[00:54:15] pushes the new data to the client, and
[00:54:17] it also reduces the bandwidth usage by
[00:54:20] allowing bidirectional communication. In
[00:54:23] client-server model with HTTP, you would
[00:54:25] make, let's say, new requests per 5
[00:54:28] seconds or 10 seconds to see if there
[00:54:30] are any new data in the server, but in
[00:54:33] this scenario, you don't make any more
[00:54:35] requests other than the first one. And
[00:54:37] now, whenever there are new data, server
[00:54:39] will push it, and whenever there are no
[00:54:41] data to be requested, then you don't
[00:54:43] need to make unnecessary requests to the
[00:54:46] server.
[00:54:47] The next very common type of protocol is
[00:54:50] Advanced Message Queuing Protocol, which
[00:54:52] is an enterprise messaging protocol used
[00:54:55] for message queuing and guaranteeing
[00:54:57] delivery. In this setup, you usually
[00:55:00] have the producer, which can be either a
[00:55:02] web service or payment system or
[00:55:04] something like that. And on the other
[00:55:06] side, you have the consumer, which can
[00:55:08] be the processor of the payments or
[00:55:11] notification systems and stuff like
[00:55:13] that. So, producer publishes messages to
[00:55:17] the message broker, and here is where
[00:55:19] you have the Advanced Message Queuing
[00:55:21] Protocol. You have queues in the middle.
[00:55:23] Let's say one of these queues is for
[00:55:25] order processing. So, whenever a new
[00:55:28] order has been placed, producer
[00:55:29] publishes a message to this queue, and
[00:55:32] then whenever this consumer is free, it
[00:55:35] can pull messages from this queue and
[00:55:37] start updating the inventory and data in
[00:55:40] the database. This allows the consumer
[00:55:42] to only pull data from here whenever it
[00:55:45] has capacity. And whenever this consumer
[00:55:48] is busy with some other tasks, it leaves
[00:55:50] the message in the queue, and then later
[00:55:52] on, whenever it has some free capacity,
[00:55:55] it will pull the message and start
[00:55:57] updating the data. And when it comes to
[00:55:59] exchange types, you have direct
[00:56:01] one-on-one exchange or fan-out or
[00:56:04] topic-based communication, and we will
[00:56:06] explore these more when we come to the
[00:56:09] message queuing section.
[00:56:10] The other common type of protocol is
[00:56:13] gRPC, which works with protocol buffers.
[00:56:16] This is a high-performance RPC framework
[00:56:19] invented by Google, and it uses HTTP/2
[00:56:22] for transport, meaning the second
[00:56:24] version of the HTTP. This means that
[00:56:27] clients should support HTTP/2, otherwise
[00:56:30] this can't be used between client and
[00:56:32] server, but that's why this is most
[00:56:34] commonly used between servers. So,
[00:56:36] usually the client is another server,
[00:56:38] and we have some other microservices
[00:56:41] communicating with each other with this
[00:56:43] gRPC framework. It mainly uses protocol
[00:56:46] buffers, and it also comes with built-in
[00:56:49] streaming capacities because it uses
[00:56:51] HTTP/2.
[00:56:53] So, these are the most common types of
[00:56:55] API protocols. There are many more, but
[00:56:57] usually in 90% of cases, you would see
[00:57:00] only these protocols. And when choosing
[00:57:02] the right one, you should mainly
[00:57:04] consider the interaction patterns.
[00:57:06] Usually by default, you go with HTTP if
[00:57:09] it's just a request-response cycle, but
[00:57:11] if you're building something like
[00:57:13] real-time chat or some real-time
[00:57:14] communication, then you would need to go
[00:57:16] with WebSockets. The choice also depends
[00:57:19] from the performance requirements. So,
[00:57:21] if you have multiple servers,
[00:57:23] microservices communicating with each
[00:57:25] other, and there is an opportunity to
[00:57:27] use gRPC, for example, then you can go
[00:57:29] with it to increase the performance and
[00:57:32] speed of the communication. But it also
[00:57:34] comes down to client compatibility. For
[00:57:37] example, most browsers don't support the
[00:57:39] latest version of the HTTP, that's why
[00:57:41] gRPC isn't that very common for
[00:57:44] browser-server communication.
[00:57:46] It also comes down to the payload size,
[00:57:49] meaning the volume of the data and
[00:57:51] encoding, security needs based on the
[00:57:53] authentication, encryption, and so on,
[00:57:56] and also the developer experience, so
[00:57:58] the tooling and documentation. And it
[00:58:01] also comes down to the developer
[00:58:02] experience because you're mostly going
[00:58:04] to work with this API, and it needs to
[00:58:07] have good documentation and tooling for
[00:58:09] you to fully work with this type of API
[00:58:11] protocol. So, to recap, we have explored
[00:58:14] the role of application protocols in
[00:58:17] network stack, the HTTP and HTTPS, which
[00:58:20] are the most fundamental types of
[00:58:22] protocols, WebSockets for real-time
[00:58:25] communication, AMQP, which stands for
[00:58:28] Advanced Message Queuing Protocol, which
[00:58:30] allows us to have asynchronous
[00:58:32] communication and adding message queues
[00:58:34] between the consumer and producer, and
[00:58:37] also gRPC, which stands for Google
[00:58:39] Remote Procedure Call, and the main
[00:58:41] advantage of this is that it's
[00:58:43] high-performance RPC framework which
[00:58:45] uses HTTP/2 for transport.
[00:58:48] So, we discussed the application layer,
[00:58:50] which includes these protocols that we
[00:58:52] usually use for building APIs, but we
[00:58:55] don't know yet about this transport
[00:58:57] layer, which includes the TCP and UDP.
[00:59:00] So, in the next lesson, we are going to
[00:59:02] discuss this layer and understand which
[00:59:04] of these transport layers, whether TCP
[00:59:07] or UDP, are the best choice depending on
[00:59:10] the API that we are building. Most
[00:59:12] developers work with APIs, but never
[00:59:15] think about what's actually delivering
[00:59:17] those packets. Like, how does it happen
[00:59:19] that the request is being made from
[00:59:21] client to server, and how does this
[00:59:24] request go through the internet? That's
[00:59:26] where the second layer comes in in the
[00:59:28] OSI model, which which the transport
[00:59:30] layer that has the TCP and UDP inside of
[00:59:34] it.
[00:59:35] These are both transport layer
[00:59:36] protocols, meaning they handle how data
[00:59:39] moves from one machine to another over
[00:59:42] the network, but both are doing it very
[00:59:45] differently. In this lesson, we'll learn
[00:59:47] about these transport layer protocols.
[00:59:49] We'll start with TCP, which is the
[00:59:51] reliable but slower version. Then we'll
[00:59:54] learn about the UDP, which is In short,
[00:59:56] it's faster and unreliable version of
[00:59:59] TCP. And we'll compare both of them and
[01:00:02] decide which one we need to choose based
[01:00:04] on the API requirements.
[01:00:07] Let's start with TCP, which stands for
[01:00:09] Transmission Control Protocol. Think of
[01:00:11] it like sending a packet with a receipt,
[01:00:14] tracking, and also signature that is
[01:00:16] required. So, when you send some packets
[01:00:19] over the internet, you usually don't
[01:00:21] send all of it at once. Sometimes the
[01:00:23] data is larger. Let's say it's divided
[01:00:26] in three chunks, so you need to send
[01:00:28] them separately. The first chunk, the
[01:00:30] second chunk, and also the third chunk.
[01:00:33] So, in this case, TCP guarantees
[01:00:35] delivery of all of these three chunks.
[01:00:38] If one of these packets is lost or
[01:00:40] arrives out of order, TCP will resend or
[01:00:43] reorder it.
[01:00:45] It's also connection-based, which means
[01:00:47] that before sending any data, it
[01:00:49] performs a three-way handshake, which is
[01:00:52] establishing the connection between
[01:00:54] client and server.
[01:00:56] It also orders these packets. Let's say
[01:00:58] the client receives the first packet
[01:01:00] first, then the third packet, then the
[01:01:03] second packet. It makes sure that it's
[01:01:05] reordered to first, second, and third.
[01:01:08] This, of course, adds overhead, but it
[01:01:10] ensures that it's accurate and reliable.
[01:01:13] That's why APIs that involve payments,
[01:01:16] authentication, or user data always use
[01:01:18] TCP. On the other hand, we have UDP,
[01:01:21] which stands for User Datagram Protocol.
[01:01:24] It's fast and efficient, but the
[01:01:26] downside of this is that it doesn't
[01:01:28] guarantee that all of the packets will
[01:01:30] arrive. For example, if you're sending
[01:01:33] four packets from the server to the
[01:01:35] client, one of these packets might be
[01:01:37] lost, and it won't be pushed to the
[01:01:39] client, and UDP won't make sure that
[01:01:42] this eventually gets delivered. So,
[01:01:44] there is no delivery guarantee. There is
[01:01:47] also no handshake or connection or any
[01:01:50] sort of tracking. But because of these
[01:01:52] tradeoffs, it is faster transmission,
[01:01:55] and it comes with less overhead as it
[01:01:57] doesn't need to make sure that all of
[01:01:59] the packets are delivered or in the
[01:02:01] correct order. For example, in video
[01:02:04] calls, UDP can be the best protocol
[01:02:06] because if some information was cut in
[01:02:09] the middle, or let's say you're in a
[01:02:11] call with someone and their internet
[01:02:13] connection lags, you don't need to
[01:02:15] receive that old connection or the old
[01:02:18] data on what they said because you are
[01:02:20] in the call right now. So, UDP is the
[01:02:22] go-to for video calls, online games, or
[01:02:25] live streams because if one of these
[01:02:27] packets drops, it's still fine, and you
[01:02:30] don't need to go back and resend this
[01:02:32] packet. You can just move on and send
[01:02:34] the next packets.
[01:02:36] This is what the three-step handshake
[01:02:38] looks like in TCP. As you can see, the
[01:02:41] first step is that client sends a
[01:02:42] request to the server. In the second
[01:02:45] step, server syncs and acknowledges the
[01:02:47] request. And in the first step, the
[01:02:50] client acknowledges the server. And this
[01:02:52] is where the connection is established
[01:02:54] between the client and server. And now
[01:02:56] they can start sending data back and
[01:02:58] forth on top of this TCP protocol.
[01:03:02] So, in short, TCP is the safer and
[01:03:04] reliable version of UDP, but it is
[01:03:07] slower. And on the other hand, UDP is
[01:03:10] faster and lightweight, but it is risky.
[01:03:13] For example, if one of the packets in
[01:03:15] between the source and destination is
[01:03:17] lost, it doesn't resend it, so there is
[01:03:19] no guaranteed delivery. But on the other
[01:03:22] hand, if in TCP one of the packets is
[01:03:24] lost, after some timeout, it still
[01:03:27] resends the third packets. And this way,
[01:03:29] it guarantees that all data will be
[01:03:31] delivered compared to UDP, where some
[01:03:34] data might be lost, but it will still
[01:03:36] keep going. And when choosing between
[01:03:38] those two, these are the main things
[01:03:40] that you need to look for. If you need
[01:03:42] the connection to be safe and reliable,
[01:03:45] then you need to go with TCP. Or if you
[01:03:47] need it to be fast, lightweight, but
[01:03:49] some data loss might be acceptable, then
[01:03:51] you will need to go with UDP. For
[01:03:54] example, it is best for using TCP in
[01:03:57] bankings, emails, payments, and so on.
[01:04:00] And on the other hand, UDP is mostly
[01:04:02] used in video streaming, streaming,
[01:04:04] gaming, and so on.
[01:04:06] These are the main things that you need
[01:04:08] to know about the application and
[01:04:10] transport layers. And these are the only
[01:04:12] layers that we'll need to be used to
[01:04:14] building APIs. And in the next lesson,
[01:04:17] we will learn about RESTful APIs and how
[01:04:20] we usually design APIs in RESTful
[01:04:22] format. RESTful APIs let different parts
[01:04:25] of a system talk to each other using the
[01:04:28] standard HTTP methods. They are the most
[01:04:31] common way developers build and consume
[01:04:33] APIs today. And in this video, you'll
[01:04:36] learn how to design clean REST APIs by
[01:04:38] following the proven best practices so
[01:04:41] that you avoid creating messy and
[01:04:43] inconsistent patterns that make the APIs
[01:04:46] hard to use and maintain. We'll start by
[01:04:49] learning about the architectural
[01:04:51] principles and constraints of RESTful
[01:04:53] APIs, about the resource modeling and
[01:04:57] URL design, also the status codes and
[01:05:00] the error handling, as well as
[01:05:02] filtering, sorting, and so on.
[01:05:04] And we'll learn the best practices when
[01:05:06] using and developing RESTful APIs.
[01:05:10] Let's start from the resource modeling.
[01:05:12] Resources are the core concepts in REST.
[01:05:15] Let's say you have the business domain,
[01:05:17] which consists of the products, orders,
[01:05:19] and reviews. When modeling these to a
[01:05:22] RESTful API, you usually convert these
[01:05:25] into nouns and not verbs, meaning that
[01:05:27] the product becomes products, order
[01:05:30] becomes orders, and same for the
[01:05:32] reviews. These can be collections or
[01:05:35] individual items. For example, this
[01:05:37] first request, which is to {slash} API
[01:05:40] {slash} products, will return you the
[01:05:42] collection of products, not a single
[01:05:44] product. But on the other hand, you
[01:05:46] could have {slash} products and {slash}
[01:05:48] specific ID of a product, which will
[01:05:50] return you the individual item.
[01:05:53] And notice that we are using {slash}
[01:05:55] products when retrieving the collection
[01:05:57] of products, and we are not using
[01:06:00] something like get products, which will
[01:06:02] be not a best practice in RESTful APIs.
[01:06:05] As I mentioned, we are using nouns here
[01:06:08] and not verbs. So, to fetch orders, for
[01:06:10] example, you don't define the URL as get
[01:06:13] orders. You just define it as {slash}
[01:06:16] orders, and depending on the method that
[01:06:18] we'll use, let's say it's a get method,
[01:06:20] then you will retrieve the orders. If
[01:06:22] it's a post method, then you will create
[01:06:24] an order, and so on.
[01:06:26] So, all the resources should be clearly
[01:06:28] identifiable through the URLs. For
[01:06:31] instance, this is an example of getting
[01:06:34] a collection. This is an example of
[01:06:36] getting a specific item. And also,
[01:06:39] nested resources should be clearly
[01:06:41] defined. For example, if you want to
[01:06:43] retrieve reviews for some specific
[01:06:45] product, then we would assume that if
[01:06:47] you make a request to {slash} products
[01:06:50] {slash} ID of that product and then
[01:06:52] {slash} reviews, you would get the
[01:06:54] reviews for that specific product. But
[01:06:57] in real-world APIs, you rarely want to
[01:06:59] return all the results at once. That's
[01:07:02] why we usually incorporate filtering,
[01:07:04] sorting, and pagination in APIs. So,
[01:07:07] let's start from the filtering. For
[01:07:09] example, if you make a request to get
[01:07:11] all the products, you usually add some
[01:07:13] query parameter, which in this case you
[01:07:15] can see it's category. So, you're first
[01:07:17] of all filtering them by category. And
[01:07:20] then also with the and sign, you add
[01:07:23] that they should be in stock, so the in
[01:07:25] stock should be true. And this way, you
[01:07:28] are only returning the items that you're
[01:07:30] going to display on the UI, and you're
[01:07:33] not making some requests that will waste
[01:07:35] the bandwidth of this API, and also it
[01:07:38] will be a huge response for you in the
[01:07:40] front-end side. Next, we also have
[01:07:42] sorting. In this case, again, it's
[01:07:44] controlled through the query parameters.
[01:07:46] And query parameters are anything that
[01:07:48] start after the question mark in the
[01:07:51] URL. So, in this case, you usually pass
[01:07:53] the sort attribute. And this can be, for
[01:07:56] example, ascending by price, or
[01:07:59] ascending by reviews, or it can be also
[01:08:01] the descending order. So, based on this,
[01:08:04] you will get the response from the API
[01:08:07] in a sorted order because if you, for
[01:08:09] example, have 1,000 items in the back
[01:08:12] end, in the database, you don't want to
[01:08:15] retrieve all of these in unsorted order
[01:08:17] to the front end because, let's say, the
[01:08:19] front end now needs to sort them by the
[01:08:22] price ascending. This means that it
[01:08:24] needs to make request to get all of the
[01:08:26] products, which are these 1,000 items
[01:08:29] that you have in the database. So, that
[01:08:32] will be very inefficient. That's why we
[01:08:34] do the sorting in the back end instead.
[01:08:36] So, your back end should support sorting
[01:08:38] functionality. This way, the front end
[01:08:41] can just make a request to your back end
[01:08:43] and pass this sort query parameter, and
[01:08:46] then that way, it will get the sorted
[01:08:48] products to be displayed on the screen.
[01:08:51] And next, we also have pagination.
[01:08:53] Again, with a query parameter, you
[01:08:55] usually pass the page which you want to
[01:08:57] retrieve, and also the limit because if
[01:09:00] you don't pass the limit, then again, it
[01:09:02] will give you all of the products
[01:09:04] starting from the page two till the end,
[01:09:07] which can be a lot of items. So, you
[01:09:09] also pass some sort of limit, and that
[01:09:11] limit is whatever you're going to
[01:09:13] display on the front end. And then based
[01:09:15] on that, you will get the response. And
[01:09:17] here, let's say you fetched 10 items, so
[01:09:20] you're going to display those 10 on the
[01:09:22] UI. And then once they click on the next
[01:09:24] page, you will make another request to
[01:09:26] the page three this time and you will
[01:09:29] get the next items from the server.
[01:09:31] Now usually we use page for pagination,
[01:09:34] but there is another common attribute
[01:09:36] that is offset. So some APIs use offset
[01:09:39] instead of the page and they use this in
[01:09:42] combination with limit which basically
[01:09:44] means if you have 1,000 items, so offset
[01:09:47] will tell the API from where to start
[01:09:50] counting these 1,000 items and the limit
[01:09:53] is the same as you have it here. So it's
[01:09:55] basically limiting the number of items
[01:09:58] that you are getting from this offset to
[01:10:00] retrieve to the front end. And the last
[01:10:03] option, you can also have this cursor
[01:10:05] based. So instead of page and limit, you
[01:10:07] would pass a cursor which will be the
[01:10:09] hash of the page you want to retrieve.
[01:10:12] So this approach of adding filtering,
[01:10:14] sorting, and pagination comes with
[01:10:16] benefits. So first of all, it saves the
[01:10:19] bandwidth of your server. It also
[01:10:21] improves the performance both in the
[01:10:23] server side and on the front end side
[01:10:25] and it also gives the front end more
[01:10:27] flexibility because now you can fetch
[01:10:29] only the things that you need and not
[01:10:32] some unnecessary data from the database.
[01:10:35] Now let's come to the HTTP methods that
[01:10:37] REST APIs use because they rely on HTTP
[01:10:40] protocols and hence they are using the
[01:10:43] HTTP methods especially for CRUD
[01:10:46] operations. So these are the most common
[01:10:49] types of CRUD operations you would see
[01:10:51] in REST APIs. First of all, we have the
[01:10:54] GET method which is used for reading
[01:10:56] data from the API. So this is for
[01:10:59] retrieving resources as you saw like
[01:11:01] retrieving the products, retrieving the
[01:11:03] reviews, and so on. And the URL usually
[01:11:06] looks like this. You make a GET request
[01:11:09] to the /api/version
[01:11:11] of the API/the resource name. And these
[01:11:14] types of requests are both safe and item
[01:11:17] potent which basically means if you make
[01:11:20] a request to /products two or three
[01:11:22] times, you expect to receive the exact
[01:11:25] same output every time unless some new
[01:11:28] products obviously have been added to
[01:11:30] the database. Next, we have the POST
[01:11:33] method. This is usually when you're
[01:11:34] creating a resource in your server. The
[01:11:37] common example is again you will make
[01:11:39] the request to exact same endpoint as
[01:11:42] you have it for the GET to create a
[01:11:44] collection, but in this case instead of
[01:11:46] GET, you are using POST method and this
[01:11:49] tells the API that you need to create a
[01:11:51] resource in the products and not
[01:11:54] retrieve them. These types of requests
[01:11:56] change the state of the server. They are
[01:11:58] adding a new item and also they are not
[01:12:01] item potent which means that they are
[01:12:03] creating a resource. So the first time
[01:12:05] you create a resource, you will get the
[01:12:07] ID of the first item that you created.
[01:12:10] The second time you create it, you will
[01:12:12] get the ID of the second one and so on.
[01:12:15] Next, we have the PUT and PATCH methods
[01:12:18] which are very similar and they are
[01:12:20] updating resources in your API, but they
[01:12:23] do it a bit differently. The PUT method
[01:12:26] replaces the whole resource, whereas the
[01:12:28] PATCH method partially updates the
[01:12:31] resource in your API. Now you can see
[01:12:33] that the request URL is exactly the same
[01:12:36] in both of their cases. So it's to
[01:12:38] /products/ID
[01:12:39] of a product you want to modify. Just in
[01:12:42] case of the PUT request, it will take
[01:12:44] this whole product with the ID of 123
[01:12:48] and it will basically replace it with
[01:12:50] the new one that is coming from the
[01:12:52] front end. Whereas in case of the PATCH,
[01:12:54] it will again take this item from the
[01:12:56] database with ID 123, but it will update
[01:13:00] it partially. Let's say you just updated
[01:13:02] the title from the front end and you
[01:13:04] made the request with PATCH method. So
[01:13:07] this will only update the title of this
[01:13:10] product and it will leave the other
[01:13:12] parts, other properties unchanged. And
[01:13:15] the last CRUD operation is DELETE and we
[01:13:17] use DELETE method in this case. And
[01:13:20] obviously as the name tells, it deletes
[01:13:22] the resource from the database. So
[01:13:25] again, the URL is exactly the same as
[01:13:27] you have for modifying items. It's to
[01:13:30] /products/ID of the resource. And in
[01:13:33] this case, you are not passing anything
[01:13:35] in the request body. So you are just
[01:13:37] making a DELETE request to this item and
[01:13:40] you are removing this from the database.
[01:13:42] And each of these operations return you
[01:13:44] different status codes depending on how
[01:13:47] the request went, whether it was
[01:13:49] successful or not. For that, we have
[01:13:51] status codes and error handling in
[01:13:54] RESTful APIs.
[01:13:55] So you should use the appropriate status
[01:13:58] codes when working with REST APIs. For
[01:14:00] example, the 200 series are for
[01:14:02] successful requests. For example, 200 is
[01:14:05] okay, 201 is resource has been created,
[01:14:09] 204 is there is no content here.
[01:14:12] Let's say you made a request, the
[01:14:14] previous request we were talking about
[01:14:16] to /products/some
[01:14:18] ID of a product and you successfully
[01:14:20] retrieved this item. This means that you
[01:14:22] also need to set the status code to 200
[01:14:25] because the request has been successful.
[01:14:28] In the other case where you're creating
[01:14:30] a product and you're making a POST
[01:14:32] request to /products, this time you
[01:14:34] shouldn't respond with the same 200 code
[01:14:37] because 200 generally means that the
[01:14:39] status was okay, but in 201 case, it
[01:14:43] means that the resource has been
[01:14:44] created. And in this case, since you're
[01:14:46] creating a new product, you should
[01:14:48] obviously respond with the 201 status
[01:14:50] code meaning resource has been created.
[01:14:53] We also have 300 series which are for
[01:14:55] redirection. Let's say you make a
[01:14:57] request to a URL and now this URL has
[01:15:00] been moved to somewhere else. So it will
[01:15:02] respond with a 300 series and it will
[01:15:05] redirect you to the new URL. In 400
[01:15:08] series, we have the client errors. So
[01:15:11] this is whenever your front end made a
[01:15:13] bad request or the user made a bad
[01:15:15] request. For example, 400 is a generic
[01:15:18] bad request. In 401, we have
[01:15:20] unauthorized requests meaning the user
[01:15:23] is not authenticated to make this
[01:15:25] request. For 404, we have not found. So
[01:15:28] generally when you visit some URL or you
[01:15:31] make a request for some specific
[01:15:33] resource that doesn't exist, you would
[01:15:35] get this 404 status code.
[01:15:37] So for 400 case, let's say you made a
[01:15:40] request with invalid parameters or some
[01:15:43] wrong JSON format. In this case, you
[01:15:45] would get a generic 400 bad request. But
[01:15:49] if a user makes a request to to get some
[01:15:51] product which is let's say the product
[01:15:54] with this ID and it doesn't exist in the
[01:15:56] database after querying it, then you
[01:15:59] should respond with the 404 status code
[01:16:01] meaning that the resource has not been
[01:16:03] found.
[01:16:04] And lastly, we have 500 series. These
[01:16:07] are things when error happens in your
[01:16:09] server. So you don't know the exact
[01:16:11] reason and it's also not a client error
[01:16:14] meaning client requested everything
[01:16:16] properly. And in this case, we throw
[01:16:19] unexpected server side errors. You
[01:16:21] generally respond with a server error
[01:16:23] message and you return the 500 status
[01:16:26] code along with it.
[01:16:28] When it comes to best practices of
[01:16:30] RESTful APIs, first of all, notice that
[01:16:32] we are using plural nouns for all of the
[01:16:35] resources. So instead of /product, we
[01:16:38] are using /products for retrieving the
[01:16:41] products collection. So you should
[01:16:43] always use the plural in this case.
[01:16:46] Also in the CRUD operations, we use the
[01:16:48] proper HTTP methods. For example, when
[01:16:51] making a request to delete users, we
[01:16:54] expect to make a request to users/ID of
[01:16:56] a user and not some POST request to
[01:16:59] /users/ID.
[01:17:01] So first of all, the HTTP methods needs
[01:17:03] to be properly set up and also the URL.
[01:17:07] We don't expect some random things like
[01:17:09] /delete to delete a resource from the
[01:17:12] database.
[01:17:13] As you saw, we also support filtering,
[01:17:15] sorting, and pagination in good REST
[01:17:18] APIs. Not only pagination. For example,
[01:17:21] in this case, we only have the page
[01:17:23] three, but we cannot limit the amount of
[01:17:25] products that we want to retrieve.
[01:17:27] Whereas in this case, we can fully
[01:17:29] control what we want to get from the
[01:17:31] API. We want to get the items from page
[01:17:34] three. We want this number of limit to
[01:17:36] be applied on the products and we also
[01:17:39] want to apply some sort like sorting to
[01:17:42] sort the price or sort by ratings and so
[01:17:45] on. And also versionings in the RESTful
[01:17:48] APIs. As you noticed in all of these
[01:17:50] requests, they all come with a prefix
[01:17:52] which is /api and then /the ID of the
[01:17:56] API which is either V1, V2, V3, and so
[01:18:00] on. Let's let's say in the future you
[01:18:03] migrate your API and you start using
[01:18:05] bunch of new features, but you also
[01:18:07] break something in the previous version
[01:18:09] one. Then if you use the versioning, you
[01:18:12] won't break it on the front end because
[01:18:13] they can use the old version of your API
[01:18:16] and still use the old features and
[01:18:18] functionalities while you continue to
[01:18:20] develop the new version, let's say
[01:18:22] version three, and you support new
[01:18:24] features here and you might have broken
[01:18:26] something here, but they are still using
[01:18:28] the old API. So this doesn't impact the
[01:18:31] end users. So to recap, we learned about
[01:18:34] the REST architectural principles and
[01:18:37] constraints, also about the resource
[01:18:39] modeling and URL design, and how we
[01:18:42] model the business domain into the
[01:18:44] RESTful API domain. Also the status
[01:18:47] codes, error handling, and the proper
[01:18:50] methods to be used with the basic CRUD
[01:18:53] operations.
[01:18:54] And lastly, we covered the best
[01:18:56] practices for RESTful APIs that you
[01:18:58] should use to keep your APIs consistent
[01:19:01] and also predictable for other
[01:19:03] developers who are using it. Traditional
[01:19:06] RESTful APIs often return too much or
[01:19:09] too little data which requires us to do
[01:19:11] multiple requests for a single view to
[01:19:14] get all the data that we need. GraphQL
[01:19:16] solves this issue by giving clients
[01:19:18] exactly what they requested for, but
[01:19:20] designing GraphQL APIs is different from
[01:19:23] designing RESTful APIs. That's why in
[01:19:25] this video we'll cover the core concepts
[01:19:27] of GraphQL and why it exists, the schema
[01:19:30] design and type system of GraphQL,
[01:19:33] queries and mutations, error handling,
[01:19:36] and also best practices for designing
[01:19:38] GraphQL APIs. Let's start by
[01:19:40] understanding why GraphQL exists in the
[01:19:42] first place. It was created by Facebook
[01:19:45] to solve a very specific pain, which is
[01:19:47] clients needing to make multiple API
[01:19:50] calls and still not getting the exact
[01:19:52] data that they needed. For example, if
[01:19:54] we imagine we have the Facebook APIs
[01:19:57] like user API, posts API, comments and
[01:20:00] likes for the Facebook page. Most of the
[01:20:02] times client can make requests to all of
[01:20:05] these APIs separately and still not get
[01:20:08] all the data that it needs, which will
[01:20:09] require it to do multiple requests to
[01:20:12] the same API. This, of course, adds up
[01:20:15] to the overall latency of the page
[01:20:17] because the page is still not loaded
[01:20:20] until all of these requests are made and
[01:20:22] the data is fetched. But in case of
[01:20:24] GraphQL APIs, you have a single GraphQL
[01:20:27] endpoint, so the client specifies the
[01:20:29] shape of the response and this one
[01:20:31] endpoint handles all of the data
[01:20:33] interactions. It is still an HTTP
[01:20:36] request, but as you can see, we can
[01:20:37] specify the exact data that we need. For
[01:20:40] example, we need the user with ID 1 2 3
[01:20:42] and we need only the name of the user,
[01:20:45] also posts, and from the posts we can
[01:20:47] specify only title, so we don't need the
[01:20:49] image for this view. And again, with the
[01:20:52] comments you can specify the exact data
[01:20:54] that you need within the object so that
[01:20:56] you are not doing over fetching of the
[01:20:58] data.
[01:20:59] Now, let's see the schema design and
[01:21:01] type system of GraphQL and how it's
[01:21:03] different from RESTful APIs. The schema
[01:21:05] in this case is a contract between the
[01:21:08] client and server. In schema, first of
[01:21:10] all, you have types, which can be, for
[01:21:12] example, user type that you specify and
[01:21:15] you specify all the fields that exist on
[01:21:17] this user type, which are ID, name,
[01:21:19] posts, and so on. And as you can see, if
[01:21:22] the type is not a primitive type like
[01:21:24] posts, then you can specify another type
[01:21:26] of post array, and then this post type
[01:21:29] can be defined separately.
[01:21:31] Next, we have queries to read data. So,
[01:21:34] this is the equivalent of doing get
[01:21:36] requests in RESTful API. You specify the
[01:21:39] query and the function of this query.
[01:21:41] This can be the user query which fetches
[01:21:44] the user with specific ID, and also the
[01:21:47] return type of this query, which in this
[01:21:49] case is the user type that we defined
[01:21:52] above.
[01:21:53] And GraphQLs also come with mutations.
[01:21:55] You can think of these as the equivalent
[01:21:57] to post, put, patch, and delete methods
[01:22:00] in RESTful APIs. So, anytime you are
[01:22:02] mutating a data in the database, you are
[01:22:05] making a mutation query. Here, as you
[01:22:08] can see, we have an example of create
[01:22:09] user method, which accepts name and, of
[01:22:12] course, many things in real world, and
[01:22:14] then it returns the user type that we
[01:22:16] have defined above. So, if you have good
[01:22:18] schema design in GraphQL, it should
[01:22:21] mirror your domain model and it should
[01:22:23] be intuitive and flexible.
[01:22:25] Next, once you define the schema design
[01:22:27] and type system, you can start querying
[01:22:30] and mutating data with this GraphQL API.
[01:22:33] For that, we have queries for fetching
[01:22:35] data. Again, this is like the get
[01:22:37] requests in RESTful APIs, and here you
[01:22:39] can specify exactly what you need from
[01:22:41] the user. This is the same user method
[01:22:44] that we defined there in the schema. So,
[01:22:46] here you can also specify the exact
[01:22:49] attributes like the name, posts, and
[01:22:51] from posts you need the title only, and
[01:22:54] this will make a request to your GraphQL
[01:22:55] API and return the exact data that you
[01:22:58] requested.
[01:22:59] Similarly, you can also use the
[01:23:01] mutations that you defined. For example,
[01:23:03] if you have a create post method defined
[01:23:05] as a mutation, you can use this to
[01:23:07] mutate the post, for example, setting
[01:23:10] the title and body of the post, and then
[01:23:12] you also specify what data you need to
[01:23:14] retrieve after this post is created,
[01:23:16] which is ID and title. When it comes to
[01:23:19] error handling in GraphQL APIs, this is
[01:23:22] a bit different than in RESTful APIs
[01:23:24] since GraphQL always returns 200 OK
[01:23:27] status for all responses, even if there
[01:23:30] was an error. In this case, we have to
[01:23:32] return errors field in the response,
[01:23:34] which will indicate that there was an
[01:23:36] error. So, partial data can still be
[01:23:38] returned with errors. Like in this case,
[01:23:41] we have the user, which is null, and
[01:23:42] then we have the errors field, which
[01:23:44] indicates that you have the status code
[01:23:46] 404, message not found, and path, which
[01:23:49] is the user in your schema. As you can
[01:23:52] see, in this case, you can specify the
[01:23:53] status code in the errors array. Since
[01:23:56] we are returning 200 status codes for
[01:23:58] all GraphQL requests, that's why we have
[01:24:00] the status code specifically mentioned
[01:24:02] in the errors so that we know what kind
[01:24:05] of error this is, which is user not
[01:24:07] found. There are also best practices
[01:24:09] that we normally follow when designing
[01:24:11] GraphQL APIs. First of all, the schemas
[01:24:14] that we saw, it's a good practice to
[01:24:16] keep them small and modular. Also, we
[01:24:18] should avoid deeply nested queries. For
[01:24:20] example, you can have a user and then
[01:24:23] nested post, and then within the post
[01:24:25] you can have a comment, so this can be
[01:24:27] infinitely nested. And to avoid that, we
[01:24:29] usually implement query limits depths,
[01:24:31] which is how deep you can go, like how
[01:24:34] many layers nested you can have in your
[01:24:37] data. So, you specify something like six
[01:24:39] or seven layers deep. You also use
[01:24:42] meaningful naming for types and fields
[01:24:44] so that it also makes from the client
[01:24:46] side because they both are going to use
[01:24:48] the same schema. And when mutating data,
[01:24:51] we always use the input types for
[01:24:53] mutations. Before a system can authorize
[01:24:56] or restrict anything, it first needs to
[01:24:59] know the identity of the requester.
[01:25:02] That's what authentication does. It
[01:25:03] verifies that the person or system
[01:25:05] trying to access your app is legit. And
[01:25:08] in this video, you'll learn how modern
[01:25:10] applications handle authentication from
[01:25:12] basic to bearer tokens to OAuth2
[01:25:15] authentication and JWT tokens, as well
[01:25:18] as access and refresh tokens, and also
[01:25:20] single sign-on and identity protocols.
[01:25:24] Before learning the different types,
[01:25:25] let's first understand what is
[01:25:27] authentication. Authentication basically
[01:25:30] answers who the user is and if they are
[01:25:32] allowed to access your system. So,
[01:25:35] whenever a login request is sent either
[01:25:37] by the user or another service, this is
[01:25:40] where we confirm the identity of the
[01:25:42] user and either provide them access, so
[01:25:45] approve their request, or reject it with
[01:25:47] unauthorized request.
[01:25:49] This is basically the first step before
[01:25:51] authorization begins, which is the topic
[01:25:54] of the next lesson.
[01:25:56] So, before you access any data or
[01:25:58] perform any actions on this service, the
[01:26:00] system needs to know who you are, and
[01:26:02] this is where the authentication is
[01:26:04] used.
[01:26:05] The first and simplest type of
[01:26:07] authentication is basic authentication.
[01:26:09] This is where you use username and
[01:26:11] password in combination and you send a
[01:26:14] login request, which contains the base64
[01:26:17] encoded version of username and
[01:26:19] password.
[01:26:20] This is a very simple way of encoding
[01:26:23] data and it's easily reversible. And
[01:26:26] because it's easily reversible, it's now
[01:26:28] considered insecure unless it's wrapped
[01:26:30] within HTTPS. But even with that, it is
[01:26:34] now very rarely used outside of the
[01:26:36] internal tools in the company.
[01:26:38] Next, we have bearer tokens, which are
[01:26:41] more secure compared to basic
[01:26:43] authentication. Here, you send the
[01:26:45] access token with each request instead
[01:26:47] of the username and password encoding.
[01:26:49] So, whenever the client needs to access
[01:26:52] resources, they send this token within
[01:26:54] the request, and then your API verifies
[01:26:57] or rejects the token, and if it
[01:26:59] verifies, then you send the successful
[01:27:01] response with the data that they
[01:27:03] requested.
[01:27:04] Bearer tokens are the standard approach
[01:27:06] nowadays, especially in API design,
[01:27:09] because it is fast and stateless, which
[01:27:11] makes it easy to scale those APIs.
[01:27:14] The next type is OAuth2 authentication
[01:27:17] in combination with JWT tokens. So,
[01:27:20] OAuth2 is a protocol, which is the
[01:27:23] second version of OAuth. It lets users
[01:27:26] log in through a trusted provider like
[01:27:28] Google or GitHub. So, user sends a
[01:27:31] request to access your resources, and if
[01:27:34] you allow them to authenticate with
[01:27:36] Google, basically Google sends your app
[01:27:38] a JWT token, which contains the
[01:27:40] information of this user. This is how
[01:27:42] that payload will look like. Usually,
[01:27:44] they send you the user ID or the email,
[01:27:47] the username, and more stuff, and also
[01:27:50] the expiration date for these JWT
[01:27:52] tokens.
[01:27:53] This is a signed object, which then you
[01:27:55] pass from your app to the API, and then
[01:27:58] your API will authenticate based on this
[01:28:01] information.
[01:28:02] JWTs are also stateless, similar to
[01:28:05] bearer tokens, which means that you
[01:28:06] don't need to store sessions between the
[01:28:09] requests, and each request can be
[01:28:11] executed separately. Next, we also have
[01:28:13] access and refresh types of tokens. So,
[01:28:16] modern systems use short-lived access
[01:28:18] tokens, which expire faster, and also
[01:28:21] long-lived refresh tokens, which usually
[01:28:24] expire later than the access tokens.
[01:28:27] Access tokens are used for API calls.
[01:28:30] So, whenever you want to get some data
[01:28:32] from the API, you send this access token
[01:28:34] to access the data, and refresh tokens,
[01:28:37] on the other hand, are used to renew the
[01:28:40] access tokens. So, whenever the access
[01:28:42] token expires, this is where you will
[01:28:44] use the refresh token to get a new one,
[01:28:47] a new access token behind the scenes.
[01:28:50] So, this way users won't be logged out,
[01:28:52] they will stay logged in, and also your
[01:28:55] system will stay secure because you are
[01:28:57] frequently renewing this access token.
[01:28:59] And one note here is that you should
[01:29:01] keep the refresh tokens in the server
[01:29:03] side for security reasons.
[01:29:06] And lastly, we have SSO, which stands
[01:29:08] for single sign-on and identity
[01:29:10] protocols that are used with it. Single
[01:29:13] sign-on lets users to have one login, so
[01:29:16] login once and access multiple services.
[01:29:19] For example, when you log in to Google,
[01:29:21] you can access both Gmail, Drive, and
[01:29:24] also Calendar, and all of their other
[01:29:26] services. And behind this is this SSO
[01:29:29] uses either SAML protocol or OAuth 2
[01:29:32] protocol.
[01:29:33] OAuth 2 is used more often nowadays for
[01:29:36] the modern applications to login with
[01:29:39] Google or with GitHub or any other
[01:29:41] service provider. It is a modern and
[01:29:44] JSON-based. And on the other hand, SAML
[01:29:47] uses XML-based approach. But still, SAML
[01:29:50] is very popular in the legacy systems
[01:29:53] and in companies that use things like
[01:29:55] Salesforce or internal dashboards.
[01:29:58] So, these are identity protocols, which
[01:30:00] means that they will define how apps
[01:30:02] securely exchange the user login
[01:30:04] information between each other. But
[01:30:06] authentication is just the first step
[01:30:08] before users can access your service.
[01:30:11] So, this tells you who the user is and
[01:30:13] if they are allowed to access your
[01:30:15] service. That is when they send a login
[01:30:18] request and you confirm or deny their
[01:30:20] identity. But after that, you also have
[01:30:23] the authorization step, which tells you
[01:30:25] what resources exactly this user can
[01:30:28] access to. Basically, it tells you what
[01:30:30] they can do, what the user can do in
[01:30:32] your system. And that is what we will
[01:30:34] cover next in the next video.
[01:30:37] Authorization is the step that happens
[01:30:39] after authentication once someone is
[01:30:41] logging in into our system. So, once
[01:30:44] their login request is approved, which
[01:30:46] means that the system now knows who the
[01:30:48] user is, the next step is deciding what
[01:30:50] they can do, which is the step of
[01:30:52] authorization. It needs to check what
[01:30:54] resources or actions that user has
[01:30:56] permissions to access and also what are
[01:30:59] the denied actions for this user. This
[01:31:02] is how we control security and privacy
[01:31:04] in the systems and in this video, you'll
[01:31:06] learn how applications and systems
[01:31:08] manage permissions using the three main
[01:31:11] authorization models. The first one is
[01:31:13] role-based access control. Next, we have
[01:31:16] attribute-based access control. Also,
[01:31:18] access control list, which is another
[01:31:20] way of managing authorization. Plus,
[01:31:23] you'll learn how technologies like OAuth
[01:31:24] 2 and JWTs help us to enforce those
[01:31:27] rules in practice. So, authentication
[01:31:30] happens first, which tells us who the
[01:31:32] user is and if they are allowed to
[01:31:34] access our system. But on the next step,
[01:31:36] we have authorization, which determines
[01:31:38] what you can actually do as a user in
[01:31:41] this system. If we take a look at GitHub
[01:31:43] as an example and accessing repositories
[01:31:46] on GitHub, there you have different
[01:31:48] permissions for different users. For
[01:31:50] example, user A can have write access
[01:31:52] only, which means they can only push
[01:31:54] code to this repo. But on the other
[01:31:57] hand, we can have user B and here you
[01:31:59] can grant only read access, which means
[01:32:01] they can only read this repository, but
[01:32:03] they cannot push code to it or they
[01:32:05] cannot create pull requests and so on.
[01:32:08] And on the other side, we can have also
[01:32:10] admin users, which have full control, so
[01:32:12] they can manage all the settings for the
[01:32:15] repository. They can even decide to
[01:32:17] delete this repository and so on. So,
[01:32:19] you can see that different users can
[01:32:21] have different access controls on
[01:32:23] systems. To manage these access
[01:32:25] controls, we have common authorization
[01:32:28] models. So, the one that we just looked
[01:32:30] at is the role-based authentication
[01:32:32] model, which assigns roles to users,
[01:32:34] something like admin, editor, or
[01:32:37] read-only access, write-only access. And
[01:32:39] this is the most common approach among
[01:32:42] these authorization models. But we also
[01:32:44] have attribute-based access control,
[01:32:47] which is based on the user or resource
[01:32:49] attributes. So, this is more flexible
[01:32:52] and more complex compared to the
[01:32:54] role-based authentication. And the other
[01:32:57] common approach is to have access
[01:32:58] control lists, ACL, and each resource
[01:33:01] here has its own permissions list. So,
[01:33:04] you can assign permission lists to a
[01:33:06] resource and this is what will determine
[01:33:08] what resources you can access. For
[01:33:10] example, this is a common way of
[01:33:12] managing Google Docs and we will look at
[01:33:14] this in more detail now. And each of
[01:33:17] these models has its tradeoffs, pros and
[01:33:19] cons. So, this depends on the specific
[01:33:22] system requirements, but real systems
[01:33:24] often combine also multiple models
[01:33:27] together to have more complex and more
[01:33:29] secure setup. So, first up, we have
[01:33:32] role-based access control or RBAC as an
[01:33:35] acronym. Here, users are assigned to
[01:33:38] roles and each role has a defined set of
[01:33:40] permissions. For example, as you saw
[01:33:42] with the GitHub, you can have admins and
[01:33:45] admins usually have full access to all
[01:33:47] resources. So, they can create, they can
[01:33:50] read or update resources. They can even
[01:33:52] delete resources and also manage other
[01:33:55] users in the roles. And next, you have
[01:33:57] editor, which is usually a bit less than
[01:34:00] admin. So, they can edit content like
[01:34:03] creating or reading content or updating
[01:34:05] resources, but they cannot delete
[01:34:08] resources and they cannot also manage
[01:34:10] other users.
[01:34:11] And next, you can have viewer users,
[01:34:13] which can only read data. So, they can
[01:34:16] read the resources and content, but they
[01:34:18] cannot update anything or they cannot
[01:34:21] create anything in your system.
[01:34:23] This is the most common way in
[01:34:25] authorization models and this is used in
[01:34:27] apps that you use daily, like you saw
[01:34:29] with GitHub or Stripe dashboards or CMS
[01:34:33] tools, team management tools and so on.
[01:34:36] The next model is attribute-based access
[01:34:38] control or ABAC in short. This access
[01:34:42] control goes beyond the roles. So, it
[01:34:44] uses the user attributes or resource
[01:34:47] attributes and environment conditions to
[01:34:50] define the access. Some example policy
[01:34:52] you can see here. Let's say you want to
[01:34:54] only allow access if some conditions are
[01:34:57] met. In this case, whenever the user
[01:34:59] department is set to HR and you can
[01:35:02] combine this with multiple conditions,
[01:35:04] like whenever the resource attribute
[01:35:06] equals to internal and so on. And only
[01:35:09] in this case, you allow them access and
[01:35:12] you either allow them read access or
[01:35:13] write access. So, this can also be
[01:35:15] combined with the role-based
[01:35:17] authorization.
[01:35:19] But in this case, you are checking the
[01:35:20] user model or resource model in your
[01:35:23] database and based on the attributes,
[01:35:26] you either allow or deny the access. So
[01:35:29] here, as you can see, we are checking
[01:35:30] user attributes like the department, the
[01:35:33] age or whatever you want to check here.
[01:35:36] Next, you can also combine it with
[01:35:38] resource attributes like confidentiality
[01:35:40] or the owner of the resource or
[01:35:43] classification.
[01:35:44] And this can also be combined with
[01:35:46] environments like time of the day,
[01:35:48] location, device type and so on.
[01:35:51] Since you're combining these attributes
[01:35:53] to either grant or restrict access, this
[01:35:56] is more flexible than the role-based
[01:35:58] authorization, but it requires good
[01:36:00] policy management and generally, it's
[01:36:02] more complex and you can encounter
[01:36:04] conflicts here with the attribute-based
[01:36:07] access control. The third common type is
[01:36:10] the access control lists. Instead of
[01:36:12] providing role-based access or
[01:36:14] attribute-based access, you can have
[01:36:16] access control list for the specific
[01:36:18] resource. Let's say you have a resource
[01:36:20] like a document or a JSON file and here
[01:36:23] you can have a permission list on which
[01:36:26] users can access this document. Like
[01:36:29] user Alice has only read access or user
[01:36:32] Bob has both read and write access and
[01:36:35] another user has no access to this
[01:36:37] document. So, as you can see, we're
[01:36:39] managing two things here. First of all,
[01:36:41] which users are allowed to access this
[01:36:43] document and second, what are their
[01:36:46] permissions? So, each of the users has
[01:36:48] different permissions on this document.
[01:36:51] ACLs are highly specific and also
[01:36:54] user-centric, which means it's hard to
[01:36:56] scale them well in systems with millions
[01:36:59] of users or objects unless you manage
[01:37:02] them carefully. But for example, Google
[01:37:04] Drive is one example of this, where you
[01:37:07] have documents like a Google Doc and
[01:37:10] then you share this Google Doc with your
[01:37:12] colleagues, right? So, you share someone
[01:37:14] with read access only and then you share
[01:37:16] this Doc with someone else, but now they
[01:37:18] can also edit and add comments to this
[01:37:21] document. So, this is a example of ACL,
[01:37:25] access control list, which is used in
[01:37:27] Google Drive and Google documents.
[01:37:30] This gives you more control over
[01:37:31] resources and documents, but it's also
[01:37:34] harder to scale with millions of users,
[01:37:37] but it's possible, as you can see,
[01:37:38] because Google Drive is using this for
[01:37:40] their documents, Excel sheets and so on.
[01:37:43] So, these were the access control
[01:37:45] models, but how do systems enforce those
[01:37:48] authorizations? These are where OAuth 2
[01:37:51] and JWT or access tokens come into play.
[01:37:54] So, first we have OAuth 2, which is
[01:37:57] delegated authorization, which is a
[01:37:59] protocol used when service wants to
[01:38:02] access another service's resources on a
[01:38:04] behalf of a user. For example, if you
[01:38:07] want to let a third-party app read your
[01:38:10] GitHub repositories, let's say you're
[01:38:12] deploying your app to Vercel, so you
[01:38:14] need to give Vercel control over your
[01:38:17] repository on GitHub. Instead of giving
[01:38:20] your username and password to the
[01:38:22] third-party application, which won't be
[01:38:24] secure at all because you don't know
[01:38:26] what they can do with your username and
[01:38:28] password, this way you are giving them
[01:38:30] full control. Instead, GitHub gives them
[01:38:33] the token that represents the
[01:38:35] permissions which you approved to use.
[01:38:37] So, you as a user send the request with
[01:38:40] the third-party app to request access to
[01:38:43] your repositories and then GitHub gives
[01:38:46] you the access token, which you should
[01:38:48] create. So, you should also provide what
[01:38:50] resources, what repositories this
[01:38:53] third-party app can access and also what
[01:38:55] they can do. Can they create, read,
[01:38:57] update or can they delete or whatever
[01:38:59] the permissions you set? And then GitHub
[01:39:02] sends them the token, which contains the
[01:39:04] permissions which this third-party app
[01:39:06] is allowed to use. And OAuth 2 defines
[01:39:09] the flow for securely issuing and
[01:39:11] validating those tokens. So, you give
[01:39:14] them the access token and not your
[01:39:16] password, which represents the
[01:39:18] permissions that you approved
[01:39:20] personally. So, it can be reading
[01:39:21] specific repos or also creating pushing
[01:39:25] to those repositories, but not deleting
[01:39:27] those repositories. And next, we have
[01:39:29] also token-based authorization using JWT
[01:39:33] or bearer tokens and permission logic.
[01:39:35] Once a user is authenticated, most
[01:39:38] systems use a token, typically a JWT
[01:39:41] token or this can be also bearer token
[01:39:43] that carries this information like user
[01:39:46] ID, the roles like admin or editor, and
[01:39:49] also scopes, which is what scopes they
[01:39:51] are allowed to access, and whenever this
[01:39:54] token is expiring and who is the issuer
[01:39:57] of this token. So, whenever a user makes
[01:40:00] a request, it always carries this token
[01:40:02] information and reaches to the backend
[01:40:05] server. This is where the server will
[01:40:07] check your token and validity, and it
[01:40:10] will apply the appropriate permission
[01:40:12] logic. So, to not confuse this with
[01:40:14] authorization models, there is a key
[01:40:16] distinction. The token usually carries
[01:40:18] the identity and claims of your user, as
[01:40:21] you see it here, but authorization
[01:40:23] models like role-based or
[01:40:25] attribute-based, this is what defines
[01:40:27] what is allowed to access as a user. So,
[01:40:31] tokens are just mechanisms, while these
[01:40:33] are authorization models. So, in
[01:40:35] summary, authorization isn't just
[01:40:37] letting users in like authentication,
[01:40:40] but it also controls what they can
[01:40:42] access once they are in.
[01:40:43] We learned what authorization is, what
[01:40:46] are the three most common authorization
[01:40:48] models, which are role-based,
[01:40:50] attribute-based, and access control
[01:40:52] lists, and also you saw couple of
[01:40:54] real-world examples, like how GitHub
[01:40:56] manages your authorization tokens, and
[01:40:58] this should give you an idea on when to
[01:41:00] use each model based on the system that
[01:41:03] you're building. And you also saw some
[01:41:05] implementation patterns with OAuth 2 or
[01:41:08] JWT tokens. Each of these models has
[01:41:10] their own tradeoffs, their own pros and
[01:41:13] cons, and real systems often combine
[01:41:15] multiple models to stay flexible and
[01:41:18] secure. APIs are like doors into your
[01:41:20] system. If you leave them unprotected,
[01:41:23] then attackers and anyone can walk right
[01:41:25] in and do whatever they want with your
[01:41:27] user data and overall the system. That's
[01:41:30] why in today's video, we'll look at
[01:41:32] seven proven techniques which will help
[01:41:34] you to protect your APIs from unwanted
[01:41:36] attacks.
[01:41:37] The first one we have in the list is
[01:41:39] rate limiting, which controls how many
[01:41:41] requests a client can make in a given
[01:41:44] time. For example, you can set a limit
[01:41:46] for user A to make, let's say, 100
[01:41:49] requests per some period of time to your
[01:41:52] API. And if they cross that limit and,
[01:41:55] let's say, make 101 requests, then you
[01:41:57] block the next request and allow some
[01:42:00] time to pass before they can send their
[01:42:02] next request. If you don't set this to
[01:42:05] your API, then attackers can overwhelm
[01:42:07] your system. They can send like
[01:42:09] thousands of requests per minute and
[01:42:12] then overwhelm your API, which will take
[01:42:14] your system down or it can also brute
[01:42:16] force your data. And these rate limits
[01:42:18] can be set per endpoint. For instance,
[01:42:21] let's say you have some {slash} comments
[01:42:23] endpoint, and here they can send a
[01:42:25] request to either create a comment or
[01:42:27] fetch comments. You can set that limit
[01:42:29] for endpoint level. So, this comments
[01:42:32] endpoint will be set to some strict
[01:42:35] number of requests per minute. You can
[01:42:38] also set it per user or IP address.
[01:42:40] Let's say in A, we have the IP address
[01:42:43] of first user, and then B for the
[01:42:45] second, C for this one, and your
[01:42:47] attacker has some IP address which
[01:42:49] corresponds to D.
[01:42:51] If you get the 101st request from the D
[01:42:55] IP address, then you will know that this
[01:42:57] user overused the API, so you will block
[01:43:00] it at the user IP level.
[01:43:03] And there is also overall rate limiting
[01:43:05] to protect from DDoS attacks. Since you
[01:43:08] can set the rate limit to work per user
[01:43:10] or per IP address, that means that this
[01:43:13] attacker alone cannot send that many
[01:43:15] requests. You will block it with your
[01:43:17] rate limiting in the API. But what they
[01:43:20] can do is they can spin up some bots,
[01:43:22] and each bot will have their own limit,
[01:43:25] right? Let's say you've set it to 100
[01:43:27] per IP address. So, each of these bots
[01:43:30] has 100, and overall they have more than
[01:43:32] you would allow or your system could
[01:43:35] handle. That's why you have also overall
[01:43:37] rate limitings, which can be some bigger
[01:43:40] number. So, whenever all the traffic
[01:43:42] coming into your server reaches or
[01:43:45] passes this number, then you will
[01:43:47] temporarily block all requests until you
[01:43:49] find out the root cause. And of course,
[01:43:52] these numbers are just examples, so in
[01:43:54] reality, it's much more than 1,000, but
[01:43:57] that's just an example.
[01:43:58] The second one on the list is CORS,
[01:44:00] which stands for cross-origin resource
[01:44:02] sharing. This controls which domain can
[01:44:05] call your API from a browser, and
[01:44:08] without proper CORS, malicious websites
[01:44:10] could trick users' browsers into making
[01:44:13] requests on their behalf. For instance,
[01:44:15] if your API is only meant to serve your
[01:44:18] front-end app, which is at
[01:44:20] app.yourdomain.com,
[01:44:22] then only requests from this source
[01:44:25] should be allowed. If anyone else sends
[01:44:27] you a request like
[01:44:28] app.anotherdomain.com,
[01:44:30] then you should block this request and
[01:44:32] not allow them to use your API for
[01:44:35] authenticating or using any of its data.
[01:44:38] The third one is also a common one,
[01:44:40] which is SQL and NoSQL injections.
[01:44:43] Injection attacks can happen when the
[01:44:45] user input is directly included in the
[01:44:48] database query. For instance, attacker
[01:44:50] can modify it and send some queries to
[01:44:53] read or delete your data.
[01:44:55] Here, for example, this part bypasses
[01:44:58] the checks entirely, and then attacker
[01:45:00] can use this query to start reading data
[01:45:03] from your database or modify anything,
[01:45:06] or they can also delete all the data,
[01:45:08] all the user data, and any other tables
[01:45:10] that you have in this database.
[01:45:13] So, to fix this, we always use
[01:45:15] parameterized queries or ORM safeguards.
[01:45:18] The next technique to use is firewalls.
[01:45:21] A firewall acts as a gatekeeper,
[01:45:24] filtering the malicious traffic from the
[01:45:26] other normal traffic. So, typically, you
[01:45:29] have it between your API and the
[01:45:31] incoming traffic. For example, if you
[01:45:34] use the AWS's web application firewall,
[01:45:37] this can block requests with unknown
[01:45:39] attack patterns, such as suspicious SQL
[01:45:42] keywords or strange HTTP methods, which
[01:45:45] means it will block any suspicious
[01:45:46] requests from attackers, but it will
[01:45:49] allow others to bypass the request and
[01:45:52] reach to your API.
[01:45:54] Some APIs are also private and should
[01:45:56] only be accessed from specific networks.
[01:45:59] That's why we have also VPNs, which
[01:46:01] stands for virtual private networks. The
[01:46:04] APIs that are within the VPN network can
[01:46:07] only be accessed by someone who is also
[01:46:09] within that same network, which means
[01:46:11] that some APIs are public-facing,
[01:46:14] meaning these APIs will allow any
[01:46:16] requests from the internet from your
[01:46:18] users.
[01:46:19] But this, for example, can be within the
[01:46:21] VPN network, which means if a user from
[01:46:24] web tries to reach your API, then this
[01:46:27] request will be blocked because the user
[01:46:30] is not within the same network. But on
[01:46:32] the other hand, if you have another user
[01:46:34] here, which is within the VPN network,
[01:46:37] they can make a request to these APIs,
[01:46:39] and in this case, they will bypass the
[01:46:41] checks, and their request will reach to
[01:46:43] your APIs.
[01:46:45] This is useful where you have internal
[01:46:47] tools. Let's say you have internal admin
[01:46:49] dashboard, and the API for this admin
[01:46:51] panel will only be reachable by
[01:46:54] employees connected to the company VPN.
[01:46:57] Next, we have CSRF, which stands for
[01:46:59] cross-site request forgery. This tricks
[01:47:02] a logged-in user's browser into making
[01:47:04] unwanted requests to the API. Let's say
[01:47:07] you as a user are logged in into your
[01:47:10] bank system, and your bank system uses
[01:47:12] cookies for authentication. If the bank
[01:47:15] system is not secure and they only use
[01:47:18] session cookies, another malicious site
[01:47:20] might use your cookie and submit a
[01:47:22] hidden transferring money request
[01:47:25] through your cookie. So, to prevent such
[01:47:27] attacks, companies also use CSRF tokens
[01:47:30] in combination with session cookie. So,
[01:47:33] the banking system will check if the
[01:47:35] session cookie is present, but it will
[01:47:37] also check if the CSRF token matches
[01:47:39] with the one that they have. And if it
[01:47:42] doesn't, then it will block this request
[01:47:44] from the other unknown source, while it
[01:47:46] will allow request from your behalf.
[01:47:49] And the last one we have is XSS, or it's
[01:47:52] also called cross-site scripting. This
[01:47:54] lets attackers to inject scripts into
[01:47:57] web pages served to other users. For
[01:48:00] example, if you have a comment section,
[01:48:02] and this comment gets submitted to your
[01:48:05] API, next, your API will also store it
[01:48:07] in a database. You can get normal
[01:48:10] requests like nice picture or something
[01:48:12] like that, and this will get to your
[01:48:14] API. Your API will store it in the
[01:48:16] database. So, everything is fine there.
[01:48:19] But what if an attacker places a script
[01:48:21] in this comment section, and within this
[01:48:24] script, they can try to do many
[01:48:26] different things. For example, they can
[01:48:28] try to fetch the cookie for another
[01:48:31] user, or they can try to inject
[01:48:33] something into your database. And if you
[01:48:36] allow this, then it will reach to your
[01:48:38] server, and the information will be
[01:48:40] written into the database. Later, when
[01:48:43] the other users load this comment
[01:48:45] section on their screen, they will get
[01:48:48] also the injected comment directly into
[01:48:50] their webpage, and the browser will
[01:48:52] execute this malicious JavaScript code
[01:48:55] into the other users' browser. These
[01:48:57] were the first two pillars of system
[01:48:59] design mastery course. If you'd like to
[01:49:01] continue learning and truly master
[01:49:03] system design and become a confident
[01:49:05] senior developer who commands six-figure
[01:49:08] salaries, you also need hands-on
[01:49:10] experience building these systems from
[01:49:12] scratch in cloud providers like AWS and
[01:49:16] explaining your architectural decisions
[01:49:18] in real interviews. For the next 7 days
[01:49:21] only, you can join the DevMastery
[01:49:23] mentorship with a 7-day free trial.
[01:49:25] You'll get the complete system design
[01:49:27] course, real-world projects, and my
[01:49:30] mentorship to become the confident
[01:49:32] senior engineer who doesn't worry about
[01:49:34] layoffs or AI taking your job because
[01:49:37] you'll have the architectural skills
[01:49:39] that companies desperately need and are
[01:49:41] always willing to pay six figures for.
[01:49:44] Click the link in the description to
[01:49:46] start your free trial today.

---
*RAW — not yet passed through D.R.D deconstruction.*
